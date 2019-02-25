# CenturyLinkCloud Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/clc** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `clc_username` - (Required) This is the CLC account username.

* `clc_password` - (Required) This is the CLC account password.

* `clc_account` - (Optional) Override CLC account alias.


## Supported Resources

* [Terraform::CLC::Group](Group.md)
* [Terraform::CLC::LoadBalancerPool](LoadBalancerPool.md)
* [Terraform::CLC::LoadBalancer](LoadBalancer.md)
* [Terraform::CLC::PublicIp](PublicIp.md)
* [Terraform::CLC::Server](Server.md)