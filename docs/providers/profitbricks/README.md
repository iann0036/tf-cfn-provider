# ProfitBricks Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/profitbricks**. The below arguments may be included as the key/value or JSON properties in the secret:

* `username` - (Required) If omitted, the `PROFITBRICKS_USERNAME` environment variable is used. The username is generally an e-mail address in 'username@domain.tld' format.

* `password` - (Required) If omitted, the `PROFITBRICKS_PASSWORD` environment variable is used.

* `endpoint` - (Optional) If omitted, the `PROFITBRICKS_API_URL` environment variable is used, or it defaults to the current Cloud API release.

* `retries` - (Deprecated) Number of retries while waiting for a resource to be provisioned. Default value is 50. **Note**: This argument has been deprecated and replaced by the implementation of resource timeouts described below.


## Supported Resources

* [Terraform::ProfitBricks::Datacenter](Datacenter.md)
* [Terraform::ProfitBricks::Firewall](Firewall.md)
* [Terraform::ProfitBricks::Group](Group.md)
* [Terraform::ProfitBricks::Ipblock](Ipblock.md)
* [Terraform::ProfitBricks::Ipfailover](Ipfailover.md)
* [Terraform::ProfitBricks::Lan](Lan.md)
* [Terraform::ProfitBricks::Loadbalancer](Loadbalancer.md)
* [Terraform::ProfitBricks::Nic](Nic.md)
* [Terraform::ProfitBricks::Server](Server.md)
* [Terraform::ProfitBricks::Share](Share.md)
* [Terraform::ProfitBricks::Snapshot](Snapshot.md)
* [Terraform::ProfitBricks::User](User.md)
* [Terraform::ProfitBricks::Volume](Volume.md)