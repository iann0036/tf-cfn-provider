# CloudStack Provider

## Configuration

To configure this resource, you may optionally create an AWS Secrets Manager secret with the name **terraform/cloudstack**. The below arguments may be included as the key/value or JSON properties in the secret:

* `api_url` - (Optional) This is the CloudStack API URL. It can also be sourced
  from the `CLOUDSTACK_API_URL` environment variable.

* `api_key` - (Optional) This is the CloudStack API key. It can also be sourced
  from the `CLOUDSTACK_API_KEY` environment variable.

* `secret_key` - (Optional) This is the CloudStack secret key. It can also be
  sourced from the `CLOUDSTACK_SECRET_KEY` environment variable.

* `config` - (Optional) The path to a `CloudMonkey` config file. If set the API
  URL, key and secret will be retrieved from this file.

* `profile` - (Optional) Used together with the `config` option. Specifies which
  `CloudMonkey` profile in the config file to use.

* `http_get_only` - (Optional) Some cloud providers only allow HTTP GET calls to
  their CloudStack API. If using such a provider, you need to set this to `true`
  in order for the provider to only make GET calls and no POST calls. It can also
  be sourced from the `CLOUDSTACK_HTTP_GET_ONLY` environment variable.

* `timeout` - (Optional) A value in seconds. This is the time allowed for Cloudstack
  to complete each asynchronous job triggered. If unset, this can be sourced from the
  `CLOUDSTACK_TIMEOUT` environment variable. Otherwise, this will default to 300
  seconds.


## Supported Resources

* [Terraform::CloudStack::AffinityGroup](docs/providers/cloudstack/AffinityGroup.md)
* [Terraform::CloudStack::Disk](docs/providers/cloudstack/Disk.md)
* [Terraform::CloudStack::EgressFirewall](docs/providers/cloudstack/EgressFirewall.md)
* [Terraform::CloudStack::Firewall](docs/providers/cloudstack/Firewall.md)
* [Terraform::CloudStack::Instance](docs/providers/cloudstack/Instance.md)
* [Terraform::CloudStack::Ipaddress](docs/providers/cloudstack/Ipaddress.md)
* [Terraform::CloudStack::LoadbalancerRule](docs/providers/cloudstack/LoadbalancerRule.md)
* [Terraform::CloudStack::NetworkAclRule](docs/providers/cloudstack/NetworkAclRule.md)
* [Terraform::CloudStack::NetworkAcl](docs/providers/cloudstack/NetworkAcl.md)
* [Terraform::CloudStack::Network](docs/providers/cloudstack/Network.md)
* [Terraform::CloudStack::Nic](docs/providers/cloudstack/Nic.md)
* [Terraform::CloudStack::PortForward](docs/providers/cloudstack/PortForward.md)
* [Terraform::CloudStack::PrivateGateway](docs/providers/cloudstack/PrivateGateway.md)
* [Terraform::CloudStack::SecondaryIpaddress](docs/providers/cloudstack/SecondaryIpaddress.md)
* [Terraform::CloudStack::SecurityGroupRule](docs/providers/cloudstack/SecurityGroupRule.md)
* [Terraform::CloudStack::SecurityGroup](docs/providers/cloudstack/SecurityGroup.md)
* [Terraform::CloudStack::SshKeypair](docs/providers/cloudstack/SshKeypair.md)
* [Terraform::CloudStack::StaticNat](docs/providers/cloudstack/StaticNat.md)
* [Terraform::CloudStack::StaticRoute](docs/providers/cloudstack/StaticRoute.md)
* [Terraform::CloudStack::Template](docs/providers/cloudstack/Template.md)
* [Terraform::CloudStack::Vpc](docs/providers/cloudstack/Vpc.md)
* [Terraform::CloudStack::VpnConnection](docs/providers/cloudstack/VpnConnection.md)
* [Terraform::CloudStack::VpnCustomerGateway](docs/providers/cloudstack/VpnCustomerGateway.md)
* [Terraform::CloudStack::VpnGateway](docs/providers/cloudstack/VpnGateway.md)