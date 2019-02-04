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
import pprint
import uuid

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

THIRD_PARTY_PROVIDERS = [
	["Abiquo", "Abiquo", "https://github.com/abiquo/terraform-provider-abiquo"],
	["Active Directory", "Active Directory", "https://github.com/GSLabDev/terraform-provider-ad"],
	["Aiven", "Aiven", "https://github.com/aiven/terraform-provider-aiven"],
	["Apigee", "Apigee", "https://github.com/zambien/terraform-provider-apigee"],
	["Artifactory", "Artifactory", "https://github.com/atlassian/terraform-provider-artifactory"],
	["Auth0", "Auth0", "https://github.com/bocodigitalmedia/terraform-provider-auth0"],
	["AVI", "AVI", "https://github.com/avinetworks/terraform-provider-avi"],
	["Aviatrix", "Aviatrix", "https://github.com/AviatrixSystems/terraform-provider-aviatrix"],
	["Azure Devops", "AzureDevops", "https://github.com/agarciamiravet/terraform-provider-azuredevops"],
	["CloudAMQP", "CloudAMQP", "https://github.com/cloudamqp/terraform-provider"],
	["CloudKarafka", "CloudKarafka", "https://github.com/cloudkarafka/terraform-provider"],
	["CloudMQTT", "CloudMQTT", "https://github.com/cloudmqtt/terraform-provider"],
	["Consul ACL", "ConsulACL", "https://github.com/Ashald/terraform-provider-consulacl"],
	["CoreOS Container Linux Configs", "CoreOSContainerLinuxConfigs", "https://github.com/coreos/terraform-provider-ct"],
	["CouchDB", "CouchDB", "https://github.com/nicolai86/terraform-provider-couchdb"],
	["Databricks", "Databricks", "https://github.com/betabandido/terraform-provider-databricks"],
	["Dead Man's Snitch", "DeadMansSnitch", "https://github.com/plukevdh/terraform-provider-dmsnitch"],
	["Digital Rebar", "DigitalRebar", "https://github.com/rackn/terraform-provider-drp/"],
	["Docker Machine", "DockerMachine", "https://github.com/gstruct/terraform-provider-dockermachine"],
	["Drone", "Drone", "https://github.com/artisanofcode/terraform-provider-drone"],
	["Dropbox", "Dropbox", "https://github.com/callensm/terraform-provider-dropbox"],
	["Duo Security", "DuoSecurity", "https://github.com/broamski/terraform-provider-duo"],
	["EfficientIP", "EfficientIP", "https://github.com/alexissavin/terraform-provider-solidserver"],
	["Elasticsearch", "Elasticsearch", "https://github.com/phillbaker/terraform-provider-elasticsearch"],
	["ElephantSQL", "ElephantSQL", "https://github.com/elephantsql/terraform-provider"],
	["ESXI", "ESXI", "https://github.com/josenk/terraform-provider-esxi"],
	["Gandi", "Gandi", "https://github.com/tiramiseb/terraform-provider-gandi"],
	["Generic Rest API", "RestAPI", "https://github.com/Mastercard/terraform-provider-restapi"],
	["Glue", "Glue", "https://github.com/MikeSouza/terraform-provider-glue"],
	["GoCD", "GoCD", "https://github.com/drewsonne/terraform-provider-gocd"],
	["Google Calendar", "GoogleCalendar", "https://github.com/sethvargo/terraform-provider-googlecalendar"],
	["Google G Suite", "GoogleGSuite", "https://github.com/DeviaVir/terraform-provider-gsuite"],
	["Hiera", "Hiera", "https://github.com/ribbybibby/terraform-provider-hiera"],
	["HTTP File Upload", "HTTPFileUpload", "https://github.com/GSLabDev/terraform-provider-httpfileupload"],
	["HP OneView", "HPOneView", "https://github.com/HewlettPackard/terraform-provider-oneview"],
	["IBM Cloud", "IBMCloud", "https://github.com/IBM-Cloud/terraform-provider-ibm"],
	["IIJ GIO", "IIJGIO", "https://github.com/iij/terraform-provider-p2pub"],
	["Infoblox", "Infoblox", "https://github.com/sky-uk/terraform-provider-infoblox"],
	["Jira", "Jira", "https://github.com/anubhavmishra/terraform-provider-jira"],
	["JumpCloud", "JumpCloud", "https://github.com/geekmuse/jumpcloud-terraform-provider"],
	["Kafka", "Kafka", "https://github.com/Mongey/terraform-provider-kafka"],
	["Keboola", "Keboola", "https://github.com/plmwong/terraform-provider-keboola"],
	["Keycloak", "Keycloak", "https://github.com/mrparkers/terraform-provider-keycloak"],
	["Kibana", "Kibana", "https://github.com/ewilde/terraform-provider-kibana"],
	["Kong", "Kong", "https://github.com/kevholditch/terraform-provider-kong"],
	["libvirt", "libvirt", "https://github.com/dmacvicar/terraform-provider-libvirt"],
	["Logentries", "Logentries", "https://github.com/dikhan/terraform-provider-logentries"],
	["Logz.io", "LogzIo", "https://github.com/jonboydell/logzio_terraform_provider"],
	["LXD", "LXD", "https://github.com/sl1pm4t/terraform-provider-lxd"],
	["Manifold", "Manifold", "https://github.com/manifoldco/terraform-provider-manifold"],
	["Matchbox", "Matchbox", "https://github.com/coreos/terraform-provider-matchbox"],
	["MongoDB Atlas", "MongoDBAtlas", "https://github.com/akshaykarle/terraform-provider-mongodbatlas"],
	["NSX-V", "NSX-V", "https://github.com/GSLabDev/terraform-provider-nsxv"],
	["Okta", "Okta", "https://github.com/articulate/terraform-provider-okta"],
	["Online.net", "OnlineNet", "https://github.com/src-d/terraform-provider-online-net"],
	["Open Day Light", "OpenDayLight", "https://github.com/GSLabDev/terraform-provider-odl"],
	["OpenAPI", "OpenAPI", "https://github.com/dikhan/terraform-provider-openapi"],
	["OpenFaaS", "OpenFaaS", "https://github.com/ewilde/terraform-provider-openfaas"],
	["oVirt", "oVirt", "https://github.com/imjoey/terraform-provider-ovirt"],
	["Pass", "Pass", "https://github.com/camptocamp/terraform-provider-pass"],
	["Pingdom", "Pingdom", "https://bitbucket.org/devops_sysops/pingdom-provider"],
	["Proxmox", "Proxmox", "https://github.com/Telmate/terraform-provider-proxmox"],
	["Puppet CA", "PuppetCA", "https://github.com/camptocamp/terraform-provider-puppetca"],
	["PuppetDB", "PuppetDB", "https://github.com/camptocamp/terraform-provider-puppetdb"],
	["QingCloud", "QingCloud", "https://github.com/yunify/terraform-provider-qingcloud"],
	["Redshift", "Redshift", "https://github.com/frankfarrell/terraform-provider-redshift"],
	["RKE", "RKE", "https://github.com/yamamoto-febc/terraform-provider-rke"],
	["Rollbar", "Rollbar", "https://github.com/babbel/terraform-provider-rollbar"],
	["SakuraCloud", "SakuraCloud", "https://github.com/sacloud/terraform-provider-sakuracloud"],
	["SCVMM", "SCVMM", "https://github.com/GSLabDev/terraform-provider-scvmm"],
	["Sentry", "Sentry", "https://github.com/jianyuan/terraform-provider-sentry"],
	["Sewan", "Sewan", "https://github.com/SewanDevs/terraform-provider-sewan"],
	["SignalFx", "SignalFx", "https://github.com/Yelp/terraform-provider-signalform"],
	["Smartronix", "Smartronix", "https://github.com/changli3/terraform-provider-smartronix"],
	["Snowflake", "Snowflake", "https://github.com/ShopRunner/terraform-provider-snowflake"],
	["Spinnaker", "Spinnaker", "https://github.com/armory-io/terraform-provider-spinnaker"],
	["Stateful", "Stateful", "https://github.com/Ashald/terraform-provider-stateful"],
	["Stripe", "Stripe", "https://github.com/franckverrot/terraform-provider-stripe"],
	["Sumo Logic", "SumoLogic", "https://github.com/SumoLogic/sumologic-terraform-provider"],
	["TeamCity", "TeamCity", "https://github.com/cvbarros/terraform-provider-teamcity"],
	["Transloadit", "Transloadit", "https://github.com/bocodigitalmedia/terraform-provider-transloadit"],
	["Updown.io", "UpdownIo", "https://github.com/mvisonneau/terraform-provider-updown"],
	["Uptimerobot", "Uptimerobot", "https://github.com/SpamapS/terraform-provider-uptimerobot"],
	["vRealize Automation", "vRealizeAutomation", "https://github.com/GSLabDev/terraform-provider-vra"],
	["Win DNS", "WinDNS", "https://github.com/PortOfPortland/terraform-provider-windns"],
	["YAML", "YAML", "https://github.com/Ashald/terraform-provider-yaml"],
	["Venafi", "Venafi", "https://github.com/Venafi/terraform-provider-venafi"],
	["Vultr", "Vultr", "https://github.com/squat/terraform-provider-vultr"],
	["ZeroTier", "ZeroTier", "https://github.com/cormacrelf/terraform-provider-zerotier"]
]

def check_call(args, cwd):
    proc = subprocess.Popen(args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=cwd)
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

    print("State File: {}/{}.tfstate".format(stack_id, physical_resource_id))

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

    # get third party plugin (if applicable)
    using_tpp = False
    tpp_path = '/tmp/' + provider_name + '/'

    for tpp in THIRD_PARTY_PROVIDERS:
        if tpp[1].lower() == provider_name:
            using_tpp = True
            master_zip_name = tpp[2].split("/")[-1] + "-master"
            
            print(check_call(['curl', '-L', tpp[2] + '/archive/master.zip', '-o', '/tmp/master.zip'], '/tmp/'))
            print(check_call(['unzip', 'master.zip', '-d', '/tmp'], '/tmp/'))
            print(check_call(['mv', master_zip_name, 'provider-' + provider_name], '/tmp/'))
            pprint.pprint(os.listdir('/tmp'))
            pprint.pprint(os.listdir('/tmp/provider-' + provider_name))

    # write file
    with open("/tmp/res.tf", "w") as f:
        f.write(terraform_file_contents)

    if request_type == "Update" or request_type == "Delete":
        # download state file
        s3file.download_file('/tmp/res.tfstate')
    
    # execute terraform apply
    if request_type == "Create":
        if using_tpp:
            print(check_call([os.environ['LAMBDA_TASK_ROOT'] + '/terraform', 'init', '-no-color', '-plugin-dir=/tmp'], '/tmp'))
        else:
            print(check_call([os.environ['LAMBDA_TASK_ROOT'] + '/terraform', 'init', '-no-color'], '/tmp'))
    if request_type == "Create" or request_type == "Update":
        print(check_call([os.environ['LAMBDA_TASK_ROOT'] + '/terraform', 'apply', '-auto-approve', '-no-color', '-state=/tmp/res.tfstate'], '/tmp'))

        with open("/tmp/res.tfstate", "r") as f:
            tfstate_str = f.read()
            s3file.put(Body=tfstate_str)

            tfstate = json.loads(tfstate_str)
            for attr_key, attr_val in tfstate['modules'][0]['resources'][next(iter(tfstate['modules'][0]['resources'].keys()))]['primary']['attributes'].items():
                attr_key = tf_to_cfn_str(attr_key)
                return_data[attr_key] = attr_val
            pprint.pprint(tfstate)
        os.remove("/tmp/res.tfstate")
    elif request_type == "Delete":
        print(check_call([os.environ['LAMBDA_TASK_ROOT'] + '/terraform', 'destroy', '-auto-approve', '-no-color', '-state=/tmp/res.tfstate'], '/tmp'))
        s3file.delete()

    return return_data


def handler(event, context):
    if 'RequestType' in event:
        # Custom::Terraform_ handler
        try:
            LOGGER.info('REQUEST RECEIVED:\n %s', event)
            LOGGER.info('REQUEST RECEIVED:\n %s', context)

            physical_resource_id = str(uuid.uuid4())
            if 'PhysicalResourceId' in event:
                physical_resource_id = event['PhysicalResourceId']

            if event['ResourceType'].startswith("Custom::Terraform_") and event['RequestType'] in ['Create', 'Update', 'Delete']:
                response_data = tf_resource_processor(
                    event['RequestType'],
                    event['LogicalResourceId'],
                    event['ResourceType'][18:].lower(),
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
        except: #pylint: disable=W0702
            LOGGER.warning('FAILED! %s %s', traceback.format_exc(), sys.exc_info()[0])
            send_response(event, context, "FAILED",
                {"Message": "Exception during processing"},
                context.log_stream_name + event['LogicalResourceId'])
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
