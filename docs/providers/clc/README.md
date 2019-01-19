# CenturyLinkCloud Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/clc**. The below arguments may be included as the key/value or JSON properties in the secret:

* `clc_username` - (Required) This is the CLC account username.

* `clc_password` - (Required) This is the CLC account password.

* `clc_account` - (Optional) Override CLC account alias.


## Supported Resources

* [Terraform::CLC::Group](docs/providers/clc/Group.md)
* [Terraform::CLC::LoadBalancerPool](docs/providers/clc/LoadBalancerPool.md)
* [Terraform::CLC::LoadBalancer](docs/providers/clc/LoadBalancer.md)
* [Terraform::CLC::PublicIp](docs/providers/clc/PublicIp.md)
* [Terraform::CLC::Server](docs/providers/clc/Server.md)