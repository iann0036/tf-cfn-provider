# Terraform CloudFormation Resource Provider

> Deploy over 2,000 new resource types with CloudFormation.

<img src="https://github.com/iann0036/tf-cfn-provider/raw/master/assets/screen1.png" width="558" height="491">

:exclamation: **CAUTION:** This project is currently in beta stages. Some resources may not work as expected and fields may not be validated.


## Installation

<a href="https://console.aws.amazon.com/cloudformation/home?#/stacks/new?&templateURL=https://s3.amazonaws.com/ianmckay-ap-southeast-2/terraform/custom_resource.yaml" target="_blank"><img src="https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png"></a>

Click the above link to deploy the stack which is required to deploy the Transform and Custom Resource handler. This is required to be in place for any future stack deployments.

If you prefer, you can also manually upsert the [custom_resource.yaml](custom_resource.yaml) stack from source and compile your own copy of the Lambda source. Please note that if you do this, the Python requirements must be vendored along with a copy of the Terraform binary.


## Usage

Once the handler stack is created, you may use the below resources by adding the `Terraform` transform to your stack. This will transform your input template to convert the Terraform:: resources into Custom Resources that will handle the lifecycle within that provider.

Most providers will require you to store credentials and/or other provider-specific settings within AWS Secrets Manager in order to access their services, generally in the secret name format **terraform/_provider-name-lowercase_**.

## Providers

Below is the list of supported providers. Click through to see provider resources and configuration details:

* [1&1](docs/providers/oneandone/README.md)
* [ACME](docs/providers/acme/README.md)
* [AWS](docs/providers/aws/README.md)
* [Alicloud](docs/providers/alicloud/README.md)
* [Arukas](docs/providers/arukas/README.md)
* [Atlas](docs/providers/atlas/README.md)
* [Azure Active Directory](docs/providers/azuread/README.md)
* [Azure Stack](docs/providers/azurestack/README.md)
* [Azure](docs/providers/azurerm/README.md)
* [Bitbucket](docs/providers/bitbucket/README.md)
* [Brightbox](docs/providers/brightbox/README.md)
* [CenturyLinkCloud](docs/providers/clc/README.md)
* [Chef](docs/providers/chef/README.md)
* [Circonus](docs/providers/circonus/README.md)
* [CloudScale](docs/providers/cloudscale/README.md)
* [CloudStack](docs/providers/cloudstack/README.md)
* [Cloudflare](docs/providers/cloudflare/README.md)
* [Cobbler](docs/providers/cobbler/README.md)
* [Consul](docs/providers/consul/README.md)
* [DNSMadeEasy](docs/providers/dme/README.md)
* [DNS](docs/providers/dns/README.md)
* [DNSimple](docs/providers/dnsimple/README.md)
* [Datadog](docs/providers/datadog/README.md)
* [DigitalOcean](docs/providers/digitalocean/README.md)
* [Docker](docs/providers/docker/README.md)
* [Dyn](docs/providers/dyn/README.md)
* [F5 BIG-IP](docs/providers/bigip/README.md)
* [Fastly](docs/providers/fastly/README.md)
* [FlexibleEngine](docs/providers/flexibleengine/README.md)
* [GitHub](docs/providers/github/README.md)
* [Gitlab](docs/providers/gitlab/README.md)
* [Google Cloud](docs/providers/google/README.md)
* [Grafana](docs/providers/grafana/README.md)
* [Hedvig](docs/providers/hedvig/README.md)
* [Heroku](docs/providers/heroku/README.md)
* [Hetzner Cloud](docs/providers/hcloud/README.md)
* [HuaweiCloud](docs/providers/huaweicloud/README.md)
* [Icinga2](docs/providers/icinga2/README.md)
* [InfluxDB](docs/providers/influxdb/README.md)
* [Kubernetes](docs/providers/kubernetes/README.md)
* [Librato](docs/providers/librato/README.md)
* [Linode](docs/providers/linode/README.md)
* [Local](docs/providers/local/README.md)
* [Logentries](docs/providers/logentries/README.md)
* [LogicMonitor](docs/providers/logicmonitor/README.md)
* [Mailgun](docs/providers/mailgun/README.md)
* [MySQL](docs/providers/mysql/README.md)
* [NS1](docs/providers/ns1/README.md)
* [Netlify](docs/providers/netlify/README.md)
* [NewRelic](docs/providers/newrelic/README.md)
* [Nomad](docs/providers/nomad/README.md)
* [Nutanix](docs/providers/nutanix/README.md)
* [OVH](docs/providers/ovh/README.md)
* [OpenStack](docs/providers/openstack/README.md)
* [OpenTelekomCloud](docs/providers/opentelekomcloud/README.md)
* [OpsGenie](docs/providers/opsgenie/README.md)
* [Oracle Cloud Infrastructure](docs/providers/oci/README.md)
* [Oracle Cloud Platform](docs/providers/oraclepaas/README.md)
* [Oracle Public Cloud](docs/providers/opc/README.md)
* [Packet](docs/providers/packet/README.md)
* [PagerDuty](docs/providers/pagerduty/README.md)
* [Palo Alto Networks](docs/providers/panos/README.md)
* [PostgreSQL](docs/providers/postgresql/README.md)
* [PowerDNS](docs/providers/powerdns/README.md)
* [ProfitBricks](docs/providers/profitbricks/README.md)
* [RabbitMQ](docs/providers/rabbitmq/README.md)
* [Rancher](docs/providers/rancher/README.md)
* [Random](docs/providers/random/README.md)
* [RightScale](docs/providers/rightscale/README.md)
* [RunScope](docs/providers/runscope/README.md)
* [Rundeck](docs/providers/rundeck/README.md)
* [Scaleway](docs/providers/scaleway/README.md)
* [Selectel](docs/providers/selvpc/README.md)
* [Skytap](docs/providers/skytap/README.md)
* [SoftLayer](docs/providers/softlayer/README.md)
* [Spotinst](docs/providers/spotinst/README.md)
* [StatusCake](docs/providers/statuscake/README.md)
* [TLS](docs/providers/tls/README.md)
* [TelefonicaOpenCloud](docs/providers/telefonicaopencloud/README.md)
* [Template](docs/providers/template/README.md)
* [TencentCloud](docs/providers/tencentcloud/README.md)
* [Terraform Enterprise](docs/providers/tfe/README.md)
* [Triton](docs/providers/triton/README.md)
* [UCloud](docs/providers/ucloud/README.md)
* [UltraDNS](docs/providers/ultradns/README.md)
* [VMware NSX-T](docs/providers/nsxt/README.md)
* [VMware vCloud Director](docs/providers/vcd/README.md)
* [VMware vSphere](docs/providers/vsphere/README.md)
* [Vault](docs/providers/vault/README.md)

## Acknowledgements

This project would not be possible without the work from the Terraform providers and the Terraform core product.
