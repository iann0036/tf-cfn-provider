import json
import logging
import signal
import requests
import boto3
import os
import traceback
import sys
import subprocess
import re
import uuid

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

def check_call(args):
    proc = subprocess.Popen(args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd='/tmp')
    stdout, stderr = proc.communicate()
    LOGGER.info(stdout)
    if proc.returncode != 0:
        LOGGER.warning(stderr)
        return stderr
    
    return False


def cfn_to_tf_str(obj):
    return re.sub('([A-Z]{1})', r'_\1', obj).lower()[1:]


def tf_to_cfn_str(obj):
    return re.sub(r'(?:^|_)(\w)', lambda x: x.group(1).upper(), obj)


def tf_format_value(obj, indent_level):
    indent = "    " * (indent_level + 1)

    if isinstance(obj, str): # string
        return "\"{}\"".format(obj)
    if str(obj).isdigit(): # int
        return obj
    if isinstance(obj, list): # list
        if len(obj) == 0:
            return "[]"
        if tf_format_value(obj[0], indent_level).startswith("{"):
            blocks = []
            for item in obj:
                blocks.append(tf_format_value(item, indent_level))
            return blocks
        else:
            params = "[\n"
            for item in obj:
                params += indent + tf_format_value(item, indent_level + 1) + ",\n"
            return params + "]"
    if isinstance(obj, dict): # dict
        params = "{\n"
        for k, v in obj.items():
            params += indent + cfn_to_tf_str(k) + " = " + tf_format_value(v, indent_level + 1) + "\n"
        return params + "}"
    
    return "{}{}".format(indent, json.dumps(obj))


def process_tf_params(resource_properties):
    params = ""

    for k, v in resource_properties.items():
        value = tf_format_value(v, 1)
        if isinstance(value, list): # blocks
            for block in value:
                params += "    {key} {value}\n".format(
                    key=cfn_to_tf_str(k),
                    value=block
                )
        else:
            params += "    {key} = {value}\n".format(
                key=cfn_to_tf_str(k),
                value=value
            )

    return params


def tf_resource_processor(request_type, logical_id, resource_type, resource_properties, physical_resource_id, stack_id):
    return_data = {}
    terraform_file_contents = ""
    provider_name = resource_type.split("_")[0]
    provider_credentials = get_secret("terraform/" + provider_name)

    s3 = boto3.resource('s3')
    s3file = s3.Object(os.environ['STATE_BUCKET'], '{}/{}.tfstate'.format(stack_id, physical_resource_id))

    LOGGER.info("State File: {}/{}.tfstate".format(stack_id, physical_resource_id))

    if provider_credentials:
        terraform_file_contents += """
provider "{provider_name}" {{

""".format(
            provider_name=provider_name
        )
        for k, v in provider_credentials.items():
            terraform_file_contents += "    " + k + " = \"" + v + "\"\n"
        terraform_file_contents += "}\n\n"

    del resource_properties['ServiceToken']
    params = process_tf_params(resource_properties)

    # generate terraform file
    terraform_file_contents += """
resource "{resource_type}" "{logical_id}" {{
{params}}}
""".format(
        resource_type=resource_type,
        logical_id=logical_id,
        params=params
    )

    # write file
    with open("/tmp/res.tf", "w") as f:
        f.write(terraform_file_contents)

    if request_type == "Update" or request_type == "Delete":
        # download state file
        s3file.download_file('/tmp/res.tfstate')
    
    # execute terraform apply
    err = check_call([os.environ['LAMBDA_TASK_ROOT'] + '/terraform', 'init', '-no-color'])
    if err:
        raise RuntimeError(err)
    
    if request_type == "Create" or request_type == "Update":
        err = check_call([os.environ['LAMBDA_TASK_ROOT'] + '/terraform', 'apply', '-auto-approve', '-no-color', '-state=/tmp/res.tfstate'])

        with open("/tmp/res.tfstate", "r") as f:
            tfstate_str = f.read()
            s3file.put(Body=tfstate_str)

            tfstate = json.loads(tfstate_str)
            resource_key = next(iter(tfstate['modules'][0]['resources'].keys()), False)
            if resource_key:
                for attr_key, attr_val in tfstate['modules'][0]['resources'][resource_key]['primary']['attributes'].items():
                    attr_key = tf_to_cfn_str(attr_key)
                    return_data[attr_key] = attr_val
            LOGGER.info(tfstate_str)
        
        os.remove("/tmp/res.tfstate")
        if err:
            raise RuntimeError(err)
    elif request_type == "Delete":
        err = check_call([os.environ['LAMBDA_TASK_ROOT'] + '/terraform', 'destroy', '-auto-approve', '-no-color', '-state=/tmp/res.tfstate'])
        if err:
            raise RuntimeError(err)
        
        s3file.delete()

    return return_data


def handler(event, context):
    if 'RequestType' in event:
        # Custom::Terraform_ handler
        try:
            LOGGER.info('REQUEST RECEIVED:\n %s', event)

            physical_resource_id = str(uuid.uuid4())
            if 'PhysicalResourceId' in event:
                physical_resource_id = event['PhysicalResourceId']

            if event['ResourceType'].startswith("Custom::Terraform_") and event['RequestType'] in ['Create', 'Update', 'Delete']:
                response_data = tf_resource_processor(
                    event['RequestType'],
                    event['LogicalResourceId'],
                    event['ResourceType'][18:].split("_")[0].lower() + "_" + cfn_to_tf_str(event['ResourceType'][18:].split("_")[1]).lower(),
                    event['ResourceProperties'],
                    physical_resource_id,
                    event['StackId'].split("/")[-1]
                )
                send_response(event, context, "SUCCESS", response_data, physical_resource_id)
            else:
                LOGGER.warning('FAILED!')
                send_response(event, context, "FAILED",
                    {"Message": "Unexpected RequestType received from CloudFormation"},
                    physical_resource_id)
        except Exception as e: #pylint: disable=W0702
            LOGGER.warning('FAILED! %s %s', traceback.format_exc(), sys.exc_info()[0])
            send_response(event, context, "FAILED",
                {"ErrorMessage": str(e)},
                physical_resource_id)
    elif 'fragment' in event:
        # Transform handler
        return handle_transform(event, context)
    else:
        LOGGER.warning('Unknown event')


def get_secret(secret_id):
    try:
        smclient = boto3.client('secretsmanager')
        credential = json.loads(smclient.get_secret_value(SecretId=secret_id)['SecretString'])
    except:
        return {}

    return credential


def send_response(event, context, response_status, response_data, physical_resource_id):
    response_object = {
        "Status": response_status,
        "PhysicalResourceId": physical_resource_id,
        "StackId": event['StackId'],
        "RequestId": event['RequestId'],
        "LogicalResourceId": event['LogicalResourceId'],
        "Data": response_data
    }

    if response_status != "SUCCESS":
        if 'ErrorMessage' in response_data:
            response_object['Reason'] = response_data['ErrorMessage']
        else:
            response_object['Reason'] = "See the details in CloudWatch Log Stream: " + context.log_stream_name
    
    response_body = json.dumps(response_object)

    LOGGER.info('ResponseURL: %s', event['ResponseURL'])
    LOGGER.info('ResponseBody: %s', response_body)

    requests.put(event['ResponseURL'], data=response_body)
    LOGGER.info('Response Sent')


def handle_transform(event, context):
    macro_response = {
        "requestId": event["requestId"],
        "status": "success"
    }

    try:
        params = {
            "params": event["templateParameterValues"],
            "template": event["fragment"],
            "account_id": event["accountId"],
            "region": event["region"]
        }
        response = event["fragment"]
        for k in list(response["Resources"].keys()):
            if response["Resources"][k]["Type"].startswith("Terraform::"):
                if "Properties" not in response["Resources"][k]:
                    response["Resources"][k]["Properties"] = {}
                response["Resources"][k]["Type"] = "Custom::" + response["Resources"][k]["Type"].replace("::","_")
                response["Resources"][k]["Properties"]["ServiceToken"] = context.invoked_function_arn
        macro_response["fragment"] = response
    except:
        LOGGER.info('Failed to process template for transform')
        macro_response["status"] = "failure"
        macro_response["errorMessage"] = "failed to process"
    
    LOGGER.info('MacroResponse: %s', json.dumps(macro_response))

    return macro_response
