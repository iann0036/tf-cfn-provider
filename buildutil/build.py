import requests
import subprocess
import os
import pprint
import json
import re


CASE_MAP = {
    'oci': 'OCI',
    'aws': 'AWS',
    'opsgenie': 'OpsGenie',
    'dnsimple': 'DNSimple',
    'vsphere': 'VSphere',
    'consul': 'Consul',
    'cloudstack': 'CloudStack',
    'tls': 'TLS',
    'cobbler': 'Cobbler',
    'azurerm': 'AzureRM',
    'nomad': 'Nomad',
    'ovh': 'OVH',
    'scaleway': 'Scaleway',
    'bitbucket': 'Bitbucket',
    'logentries': 'Logentries',
    'datadog': 'Datadog',
    'pagerduty': 'PagerDuty',
    'oneandone': 'OneAndOne',
    'chef': 'Chef',
    'ultradns': 'UltraDNS',
    'profitbricks': 'ProfitBricks',
    'postgresql': 'PostgreSQL',
    'google': 'Google',
    'dme': 'DME',
    'triton': 'Triton',
    'circonus': 'Circonus',
    'dyn': 'Dyn',
    'mailgun': 'Mailgun',
    'influxdb': 'InfluxDB',
    'alicloud': 'Alicloud',
    'rundeck': 'Rundeck',
    'grafana': 'Grafana',
    'rabbitmq': 'RabbitMQ',
    'digitalocean': 'DigitalOcean',
    'arukas': 'Arukas',
    'vcd': 'VCD',
    'powerdns': 'PowerDNS',
    'atlas': 'Atlas',
    'dns': 'DNS',
    'newrelic': 'NewRelic',
    'github': 'GitHub',
    'librato': 'Librato',
    'openstack': 'OpenStack',
    'heroku': 'Heroku',
    'packet': 'Packet',
    'clc': 'CLC',
    'template': 'Template',
    'icinga2': 'Icinga2',
    'softlayer': 'SoftLayer',
    'spotinst': 'Spotinst',
    'cloudflare': 'Cloudflare',
    'mysql': 'MySQL',
    'kubernetes': 'Kubernetes',
    'opc': 'OPC',
    'vault': 'Vault',
    'gitlab': 'Gitlab',
    'statuscake': 'StatusCake',
    'random': 'Random',
    'local': 'Local',
    'ns1': 'NS1',
    'fastly': 'Fastly',
    'docker': 'Docker',
    'rancher': 'Rancher',
    'logicmonitor': 'LogicMonitor',
    'cloudscale': 'CloudScale',
    'netlify': 'Netlify',
    'opentelekomcloud': 'OpenTelekomCloud',
    'panos': 'Panos',
    'oraclepaas': 'OraclePaaS',
    'nsxt': 'NSXT',
    'runscope': 'RunScope',
    'flexibleengine': 'FlexibleEngine',
    'hcloud': 'HCloud',
    'azurestack': 'AzureStack',
    'telefonicaopencloud': 'TelefonicaOpenCloud',
    'huaweicloud': 'HuaweiCloud',
    'brightbox': 'Brightbox',
    'tfe': 'Tfe',
    'acme': 'ACME',
    'rightscale': 'RightScale',
    'bigip': 'BIGIP',
    'tencentcloud': 'TencentCloud',
    'nutanix': 'Nutanix',
    'linode': 'Linode',
    'selvpc': 'SelVPC',
    'skytap': 'Skytap',
    'hedvig': 'Hedvig',
    'ucloud': 'UCloud',
    'azuread': 'AzureAD'
}


def tf_to_cfn_str(obj):
    return re.sub(r'(?:^|_)(\w)', lambda x: x.group(1).upper(), obj)


def check_call(args, cwd):
    proc = subprocess.Popen(args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=cwd)
    stdout, stderr = proc.communicate()
    if proc.returncode != 0:
        raise subprocess.CalledProcessError(
            returncode=proc.returncode,
            cmd=args)
    
    return stdout


def checkout(url, provider_name):
    try:
        check_call(['git', 'clone', url, '/tmp/' + provider_name + '/'], '/tmp')
    except:
        check_call(['git', 'pull', url], '/tmp/' + provider_name)


def iterate_resources(provider_name):
    path = "/tmp/{}/website/docs/r/".format(provider_name)
    if os.path.isdir(path):
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

        for filename in files:
            with open(os.path.join(path, filename), 'r') as f:
                #print(filename)
                resource_file_contents = f.read()
                process_file(provider_name, resource_file_contents)


def process_file(provider_name, file_contents):
    section = ""

    resource_type = ""
    description = ""
    example = ""
    arguments = ""
    attributes = {}

    lines = file_contents.split("\n")
    for line in lines:
        if line.startswith("# " + provider_name):
            resource_type = line[2:].replace("\\", "")
            section = "description"
        elif line == "## Example Usage":
            section = "example"
        elif line == "## Argument Reference":
            section = "arguments"
        elif line == "## Attributes Reference":
            section = "attributes"
        elif line.startswith("##"):
            section = ""
        elif section == "description":
            description += line + "\n"
        elif section == "example":
            example += line + "\n"
        elif section == "arguments":
            arguments += line + "\n"
        elif section == "attributes":
            if line.strip().startswith("* "):
                startpos = line.strip().find("`")
                endpos = line.strip().find("`", startpos+1)
                if startpos != -1 and endpos != -1:
                    attribute_name = line.strip()[startpos+1:endpos]
                    if line.strip()[endpos+1:].strip().startswith("- "):
                        attribute_description = line.strip()[endpos+1:].strip()[2:]
                        if attribute_description[-1] != ".":
                            attribute_description += "."
                        attributes[attribute_name] = attribute_description
    
    if resource_type != "":
        split_provider_name = resource_type.split("_")
        split_provider_name.pop(0)
        cfn_provider_name = provider_name
        if provider_name in CASE_MAP:
            cfn_provider_name = CASE_MAP[provider_name]
        cfn_type = "Terraform::" + cfn_provider_name + "::" + tf_to_cfn_str("_".join(split_provider_name))
        print(cfn_type)
        
        #print("!!!! Resource Type")
        #print(resource_type)
        #print("!!!! Description")
        #print(description)
        #print("!!!! Example")
        #print(example)
        #print("!!!! Arguments")
        #print(arguments)
        #print("!!!! Attributes")
        #pprint.pprint(attributes)
        #print("\n-----\n")


page = 1
repos = json.loads(requests.get("https://api.github.com/orgs/terraform-providers/repos").text)
while len(repos) > 0:
    for repo in repos:
        #print(repo['html_url'])
        checkout(repo['html_url'], repo['name'][19:])
        iterate_resources(repo['name'][19:])
    page+=1
    repos = json.loads(requests.get("https://api.github.com/orgs/terraform-providers/repos?page=" + str(page)).text)
