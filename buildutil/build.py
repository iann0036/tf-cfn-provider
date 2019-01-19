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
    resources_path = "/tmp/{}/website/docs/r/".format(provider_name)
    index_path = "/tmp/{}/website/docs/index.html.markdown".format(provider_name)
    provider_reference_path = "/tmp/{}/website/docs/provider_reference.html.markdown".format(provider_name)

    if os.path.isdir(resources_path) and provider_name in CASE_MAP:

        # make provider readme
        try:
            os.makedirs("../docs/providers/{}".format(provider_name))
        except:
            pass
        
        with open("../docs/providers/{}/README.md".format(provider_name), 'w') as provider_readme:
            readable_provider_name = CASE_MAP[provider_name][1]
            
            # provider info
            with open(index_path, 'r') as f:
                section = ""
                first_argument_found = False
                arguments = []
                index_file_contents = f.read()
                lines = index_file_contents.split("\n")
                for line in lines:
                    if line.startswith("*") and section == "arguments":
                        first_argument_found = True
                    if line.startswith("## Argument Reference") or line.startswith("## Arguments Reference") or line.startswith("## Configuration Reference") or "the following arguments:" in line or "provide the following credentials:" in line:
                        section = "arguments"
                    elif line.startswith("#"):
                        section = ""
                    elif section == "arguments" and first_argument_found:
                        arguments.append(line)
            
            # try provider reference (eg. google)
            if len(arguments) == 0:
                try:
                    with open(provider_reference_path, 'r') as f:
                        section = ""
                        first_argument_found = False
                        arguments = []
                        index_file_contents = f.read()
                        lines = index_file_contents.split("\n")
                        for line in lines:
                            if (line.startswith("*") or line.startswith("-")) and section == "arguments":
                                first_argument_found = True
                            if line.startswith("## Argument Reference") or line.startswith("## Arguments Reference") or line.startswith("## Configuration Reference") or "the following arguments:" in line or "provide the following credentials:" in line:
                                section = "arguments"
                            elif line.startswith("#"):
                                section = ""
                            elif section == "arguments" and first_argument_found and not "navigation to the left" in line:
                                if line.startswith("-"):
                                    line[0] = "*"
                                arguments.append(line)
                except:
                    pass
            
            # remove environmental variable references
            argument_text = "\n".join(arguments)
            if provider_name not in ['digitalocean', 'fastly', 'flexibleengine', 'google', 'oneandone', 'profitbricks']:
                sentences = argument_text.split(".")
                i = 0
                while len(sentences) > i:
                    if ("environment variable" in sentences[i] or "environmental variable" in sentences[i] or "Can be sourced from" in sentences[i]):
                        del sentences[i]
                    else:
                        i+=1
                argument_text = ".".join(sentences)

            has_required_arguments = False
            if "required" in argument_text.lower():
                has_required_arguments = True
            provider_readme.write("# {} Provider\n\n## Configuration\n\n".format(readable_provider_name))
            if len(arguments) == 0:
                provider_readme.write("No configuration is required for this provider.\n\n")
            elif not has_required_arguments:
                provider_readme.write("To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/{}**. The below arguments may be included as the key/value or JSON properties in the secret:\n\n".format(provider_name))
                provider_readme.write(argument_text + "\n\n")
            else:
                provider_readme.write("To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/{}**. The below arguments may be included as the key/value or JSON properties in the secret:\n\n".format(provider_name))
                provider_readme.write(argument_text + "\n\n")

            # iterate provider resources
            provider_readme.write("## Supported Resources\n\n")
            provider_readme_items = []
            files = [f for f in os.listdir(resources_path) if os.path.isfile(os.path.join(resources_path, f))]
            for filename in files:
                with open(os.path.join(resources_path, filename), 'r') as f:
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
                    if line.strip()[endpos+1:].strip().startswith("- ") or line.strip()[endpos+1:].strip().startswith("= "):
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
            provider_readme_items.append("* [{cfn_type}]({type_stub}.md)".format(
                cfn_type=cfn_type,
                provider_name=provider_name,
                type_stub=tf_to_cfn_str("_".join(split_provider_name))
            ))
        
        #print("!!!! Resource Type")
        #print(resource_type)
        #print("!!!! Description")
        description = description.strip()
        #print(description)
        #print("!!!! Example")
        #print(example)
        #print("!!!! Arguments")
        #print(arguments)
        #print("!!!! Attributes")
        #pprint.pprint(attributes)
        #print("\n-----\n")

        return_values = ""
        if attributes:
            return_values = "## Return Values\n\n### Fn::GetAtt\n\n"
            for attr in attributes:
                return_values += "`{ret}` - {desc}\n\n".format(
                    ret=tf_to_cfn_str(attr),
                    desc=attributes[attr]
                )
        
        try:
            os.makedirs("../docs/providers/{}/".format(provider_name))
        except:
            pass
        with open("../docs/providers/{}/{}.md".format(provider_name, tf_to_cfn_str("_".join(split_provider_name))), 'w') as resource_readme:
            resource_readme.write("# {cfn_type}\n\n{description}\n\n## Properties\n\nTBC\n\n{return_values}## See Also\n\n* [{provider_name}_{split_provider_name_joined}](https://www.terraform.io/docs/providers/{provider_name}/r/{split_provider_name_joined}.html) in the _Terraform Provider Documentation_".format(
                provider_name=provider_name,
                split_provider_name_joined="_".join(split_provider_name),
                cfn_type=cfn_type,
                description=description,
                return_values=return_values
            ))


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