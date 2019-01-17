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

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

def check_call(args):
    proc = subprocess.Popen(args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd='/tmp')
    stdout, stderr = proc.communicate()
    if proc.returncode != 0:
        print(stdout)
        print(stderr)
        raise subprocess.CalledProcessError(
            returncode=proc.returncode,
            cmd=args)
    
    return stdout


def cfn_to_tf_str(obj):
    return re.sub('([A-Z]{1})', r'_\1', obj).lower()[1:]


def tf_format_value(obj, indent_level):
    indent = "    " * (indent_level + 1)

    if isinstance(obj, str): # string
        return "\"{}\"".format(obj)
    if str(obj).isdigit(): # int
        return obj
    if isinstance(obj, list): # list
        params = "[\n"
        for item in obj:
            params += indent + tf_format_value(item, indent_level + 1) + ",\n"
        return params + "]"
    if isinstance(obj, dict): # list
        params = "{\n"
        for k, v in obj.items():
            params += indent + cfn_to_tf_str(k) + " = " + tf_format_value(v, indent_level + 1) + "\n"
        return params + "}"
    
    return "{}{}".format(indent, json.dumps(obj))


def process_tf_params(resource_properties):
    params = ""

    for k, v in resource_properties.items():
        params += "    {key} = {value}\n".format(
            key=cfn_to_tf_str(k),
            value=tf_format_value(v, 1)
        )

    return params


def tf_resource_processor(logical_id, resource_type, resource_properties):
    terraform_file_contents = ""

    provider_name = resource_type.split("_")[0]

    provider_credentials = get_secret("terraform/" + provider_name)
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

    print("#####")
    print(terraform_file_contents)
    print("-----")

    # write file
    with open("/tmp/res.tf", "w") as f:
        f.write(terraform_file_contents)
    
    # execute terraform apply
    print(check_call([os.environ['LAMBDA_TASK_ROOT'] + '/terraform', 'init', '-no-color']))
    print(check_call([os.environ['LAMBDA_TASK_ROOT'] + '/terraform', 'apply', '-auto-approve', '-no-color', '-state=/tmp/res.tfstate']))
    with open("/tmp/res.tfstate", "r") as f:
        print(f.read())

    return {}


def handler(event, context):
    # Setup alarm for remaining runtime minus a second
    signal.alarm(int(context.get_remaining_time_in_millis() / 1000) - 1)

    if 'RequestType' in event:
        # Custom::Terraform_ handler
        try:
            LOGGER.info('REQUEST RECEIVED:\n %s', event)
            LOGGER.info('REQUEST RECEIVED:\n %s', context)

            if event['ResourceType'].startswith("Custom::Terraform_"):
                response_data = tf_resource_processor(event['LogicalResourceId'], event['ResourceType'][18:].lower(), event['ResourceProperties'])

            if event['RequestType'] in ['Create', 'Update', 'Delete']:
                send_response(event, context, "SUCCESS", response_data)
            else:
                LOGGER.warning('FAILED!')
                send_response(event, context, "FAILED",
                    {"Message": "Unexpected RequestType received from CloudFormation"})
        except: #pylint: disable=W0702
            LOGGER.warning('FAILED! %s %s', traceback.format_exc(), sys.exc_info()[0])
            send_response(event, context, "FAILED",
                {"Message": "Exception during processing"})
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


def send_response(event, context, response_status, response_data):
    response_object = {
        "Status": response_status,
        "PhysicalResourceId": context.log_stream_name + event['LogicalResourceId'],
        "StackId": event['StackId'],
        "RequestId": event['RequestId'],
        "LogicalResourceId": event['LogicalResourceId'],
        "Data": response_data
    }

    if response_status != "SUCCESS":
        response_object['Reason'] = "See the details in CloudWatch Log Stream: " + context.log_stream_name
    
    response_body = json.dumps(response_object)

    LOGGER.info('ResponseURL: %s', event['ResponseURL'])
    LOGGER.info('ResponseBody: %s', response_body)

    requests.put(event['ResponseURL'], data=response_body)
    LOGGER.info('Response Sent')


def timeout_handler(_signal, _frame):
    raise Exception('Time exceeded')


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


signal.signal(signal.SIGALRM, timeout_handler)
