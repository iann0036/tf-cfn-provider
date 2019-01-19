import requests
import subprocess
import os
import pprint
import json
import re


CASE_MAP = {
    'oci': ['OCI','Oracle Cloud Infrastructure'],
    'aws': ['AWS','AWS'],
    'opsgenie': ['OpsGenie','OpsGenie'],
    'dnsimple': ['DNSimple','DNSimple'],
    'vsphere': ['VSphere','VMware vSphere'],
    'consul': ['Consul','Consul'],
    'cloudstack': ['CloudStack','CloudStack'],
    'tls': ['TLS','TLS'],
    'cobbler': ['Cobbler','Cobbler'],
    'azurerm': ['AzureRM','Azure'],
    'nomad': ['Nomad','Nomad'],
    'ovh': ['OVH','OVH'],
    'scaleway': ['Scaleway','Scaleway'],
    'bitbucket': ['Bitbucket','Bitbucket'],
    'logentries': ['Logentries','Logentries'],
    'datadog': ['Datadog','Datadog'],
    'pagerduty': ['PagerDuty','PagerDuty'],
    'oneandone': ['OneAndOne','1&1'],
    'chef': ['Chef','Chef'],
    'ultradns': ['UltraDNS','UltraDNS'],
    'profitbricks': ['ProfitBricks','ProfitBricks'],
    'postgresql': ['PostgreSQL','PostgreSQL'],
    'google': ['Google','Google Cloud'],
    'dme': ['DME','DNSMadeEasy'],
    'triton': ['Triton','Triton'],
    'circonus': ['Circonus','Circonus'],
    'dyn': ['Dyn','Dyn'],
    'mailgun': ['Mailgun','Mailgun'],
    'influxdb': ['InfluxDB','InfluxDB'],
    'alicloud': ['Alicloud','Alicloud'],
    'rundeck': ['Rundeck','Rundeck'],
    'grafana': ['Grafana','Grafana'],
    'rabbitmq': ['RabbitMQ','RabbitMQ'],
    'digitalocean': ['DigitalOcean','DigitalOcean'],
    'arukas': ['Arukas','Arukas'],
    'vcd': ['VCD','VMware vCloud Director'],
    'powerdns': ['PowerDNS','PowerDNS'],
    'atlas': ['Atlas','Atlas'],
    'dns': ['DNS','DNS'],
    'newrelic': ['NewRelic','NewRelic'],
    'github': ['GitHub','GitHub'],
    'librato': ['Librato','Librato'],
    'openstack': ['OpenStack','OpenStack'],
    'heroku': ['Heroku','Heroku'],
    'packet': ['Packet','Packet'],
    'clc': ['CLC','CenturyLinkCloud'],
    'template': ['Template','Template'],
    'icinga2': ['Icinga2','Icinga2'],
    'softlayer': ['SoftLayer','SoftLayer'],
    'spotinst': ['Spotinst','Spotinst'],
    'cloudflare': ['Cloudflare','Cloudflare'],
    'mysql': ['MySQL','MySQL'],
    'kubernetes': ['Kubernetes','Kubernetes'],
    'opc': ['OPC','Oracle Public Cloud'],
    'vault': ['Vault','Vault'],
    'gitlab': ['Gitlab','Gitlab'],
    'statuscake': ['StatusCake','StatusCake'],
    'random': ['Random','Random'],
    'local': ['Local','Local'],
    'ns1': ['NS1','NS1'],
    'fastly': ['Fastly','Fastly'],
    'docker': ['Docker','Docker'],
    'rancher': ['Rancher','Rancher'],
    'logicmonitor': ['LogicMonitor','LogicMonitor'],
    'cloudscale': ['CloudScale','CloudScale'],
    'netlify': ['Netlify','Netlify'],
    'opentelekomcloud': ['OpenTelekomCloud','OpenTelekomCloud'],
    'panos': ['Panos','Palo Alto Networks'],
    'oraclepaas': ['OraclePaaS','Oracle Cloud Platform'],
    'nsxt': ['NSXT','VMware NSX-T'],
    'runscope': ['RunScope','RunScope'],
    'flexibleengine': ['FlexibleEngine','FlexibleEngine'],
    'hcloud': ['HCloud','Hetzner Cloud'],
    'azurestack': ['AzureStack','Azure Stack'],
    'telefonicaopencloud': ['TelefonicaOpenCloud','TelefonicaOpenCloud'],
    'huaweicloud': ['HuaweiCloud','HuaweiCloud'],
    'brightbox': ['Brightbox','Brightbox'],
    'tfe': ['Tfe','Terraform Enterprise'],
    'acme': ['ACME','ACME'],
    'rightscale': ['RightScale','RightScale'],
    'bigip': ['BIGIP','F5 BIG-IP'],
    'tencentcloud': ['TencentCloud','TencentCloud'],
    'nutanix': ['Nutanix','Nutanix'],
    'linode': ['Linode','Linode'],
    'selvpc': ['SelVPC','Selectel'],
    'skytap': ['Skytap','Skytap'],
    'hedvig': ['Hedvig','Hedvig'],
    'ucloud': ['UCloud','UCloud'],
    'azuread': ['AzureAD','Azure Active Directory']
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
    if os.path.isdir(path) and provider_name in CASE_MAP:

        # make provider readme
        try:
            os.makedirs("../docs/providers/{}".format(provider_name))
        except:
            pass
        
        with open("../docs/providers/{}/README.md".format(provider_name), 'w') as provider_readme:
            readable_provider_name = CASE_MAP[provider_name][1]
            provider_readme.write("# {} Provider\n\n## Supported Resources\n\n".format(readable_provider_name))

            # iterate provider resources
            provider_readme_items = []
            files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
            for filename in files:
                with open(os.path.join(path, filename), 'r') as f:
                    #print(filename)
                    resource_file_contents = f.read()
                    process_file(provider_name, resource_file_contents, provider_readme_items)
            
            provider_readme_items = list(set(provider_readme_items))
            provider_readme_items.sort()
            provider_readme.write("\n".join(provider_readme_items))


def process_file(provider_name, file_contents, provider_readme_items):
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
            cfn_provider_name = CASE_MAP[provider_name][0]
            cfn_type = "Terraform::" + cfn_provider_name + "::" + tf_to_cfn_str("_".join(split_provider_name))
            provider_readme_items.append("* [{cfn_type}](docs/providers/{provider_name}/{type_stub}.md)".format(
                cfn_type=cfn_type,
                provider_name=provider_name,
                type_stub=tf_to_cfn_str("_".join(split_provider_name))
            ))
        
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

provider_list = []
for provider in CASE_MAP:
    provider_list.append("* [{provider_long_name}](docs/providers/{provider_short_name}/README.md)".format(
        provider_long_name = CASE_MAP[provider][1],
        provider_short_name=provider
    ))
provider_list.sort()
with open("./READMEResources.txt", 'w') as f:
    f.write("\n".join(provider_list))