# ProfitBricks Provider

##Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/profitbricks**. The below arguments may be included as the key/value or JSON properties in the secret:

* `username` - (Required) If omitted, the `PROFITBRICKS_USERNAME` environment variable is used. The username is generally an e-mail address in 'username@domain.tld' format.

* `password` - (Required) If omitted, the `PROFITBRICKS_PASSWORD` environment variable is used.

* `endpoint` - (Optional) If omitted, the `PROFITBRICKS_API_URL` environment variable is used, or it defaults to the current Cloud API release.

* `retries` - (Deprecated) Number of retries while waiting for a resource to be provisioned. Default value is 50. **Note**: This argument has been deprecated and replaced by the implementation of resource timeouts described below.


## Supported Resources

* [Terraform::ProfitBricks::Datacenter](docs/providers/profitbricks/Datacenter.md)
* [Terraform::ProfitBricks::Firewall](docs/providers/profitbricks/Firewall.md)
* [Terraform::ProfitBricks::Group](docs/providers/profitbricks/Group.md)
* [Terraform::ProfitBricks::Ipblock](docs/providers/profitbricks/Ipblock.md)
* [Terraform::ProfitBricks::Ipfailover](docs/providers/profitbricks/Ipfailover.md)
* [Terraform::ProfitBricks::Lan](docs/providers/profitbricks/Lan.md)
* [Terraform::ProfitBricks::Loadbalancer](docs/providers/profitbricks/Loadbalancer.md)
* [Terraform::ProfitBricks::Nic](docs/providers/profitbricks/Nic.md)
* [Terraform::ProfitBricks::Server](docs/providers/profitbricks/Server.md)
* [Terraform::ProfitBricks::Share](docs/providers/profitbricks/Share.md)
* [Terraform::ProfitBricks::Snapshot](docs/providers/profitbricks/Snapshot.md)
* [Terraform::ProfitBricks::User](docs/providers/profitbricks/User.md)
* [Terraform::ProfitBricks::Volume](docs/providers/profitbricks/Volume.md)