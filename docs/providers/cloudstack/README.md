# CloudStack Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/cloudstack**. The below arguments may be included as the key/value or JSON properties in the secret:

* `api_url` - (Optional) This is the CloudStack API URL.

* `api_key` - (Optional) This is the CloudStack API key.

* `secret_key` - (Optional) This is the CloudStack secret key.

* `config` - (Optional) The path to a `CloudMonkey` config file. If set the API
  URL, key and secret will be retrieved from this file.

* `profile` - (Optional) Used together with the `config` option. Specifies which
  `CloudMonkey` profile in the config file to use.

* `http_get_only` - (Optional) Some cloud providers only allow HTTP GET calls to
  their CloudStack API. If using such a provider, you need to set this to `true`
  in order for the provider to only make GET calls and no POST calls.

* `timeout` - (Optional) A value in seconds. This is the time allowed for Cloudstack
  to complete each asynchronous job triggered. Otherwise, this will default to 300
  seconds.


## Supported Resources

* [Terraform::CloudStack::AffinityGroup](AffinityGroup.md)
* [Terraform::CloudStack::Disk](Disk.md)
* [Terraform::CloudStack::EgressFirewall](EgressFirewall.md)
* [Terraform::CloudStack::Firewall](Firewall.md)
* [Terraform::CloudStack::Instance](Instance.md)
* [Terraform::CloudStack::Ipaddress](Ipaddress.md)
* [Terraform::CloudStack::LoadbalancerRule](LoadbalancerRule.md)
* [Terraform::CloudStack::NetworkAclRule](NetworkAclRule.md)
* [Terraform::CloudStack::NetworkAcl](NetworkAcl.md)
* [Terraform::CloudStack::Network](Network.md)
* [Terraform::CloudStack::Nic](Nic.md)
* [Terraform::CloudStack::PortForward](PortForward.md)
* [Terraform::CloudStack::PrivateGateway](PrivateGateway.md)
* [Terraform::CloudStack::SecondaryIpaddress](SecondaryIpaddress.md)
* [Terraform::CloudStack::SecurityGroupRule](SecurityGroupRule.md)
* [Terraform::CloudStack::SecurityGroup](SecurityGroup.md)
* [Terraform::CloudStack::SshKeypair](SshKeypair.md)
* [Terraform::CloudStack::StaticNat](StaticNat.md)
* [Terraform::CloudStack::StaticRoute](StaticRoute.md)
* [Terraform::CloudStack::Template](Template.md)
* [Terraform::CloudStack::Vpc](Vpc.md)
* [Terraform::CloudStack::VpnConnection](VpnConnection.md)
* [Terraform::CloudStack::VpnCustomerGateway](VpnCustomerGateway.md)
* [Terraform::CloudStack::VpnGateway](VpnGateway.md)