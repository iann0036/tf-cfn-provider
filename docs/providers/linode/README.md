# Linode Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/linode**. The below arguments may be included as the key/value or JSON properties in the secret:

* `token` - (Required) This is your [Linode APIv4 Token](https://developers.linode.com/api/v4#section/Personal-Access-Token).


## Supported Resources

* [Terraform::Linode::Domain](Domain.md)
* [Terraform::Linode::Image](Image.md)
* [Terraform::Linode::Instance](Instance.md)
* [Terraform::Linode::NodebalancerConfig](NodebalancerConfig.md)
* [Terraform::Linode::NodebalancerNode](NodebalancerNode.md)
* [Terraform::Linode::Nodebalancer](Nodebalancer.md)
* [Terraform::Linode::Sshkey](Sshkey.md)
* [Terraform::Linode::Stackscript](Stackscript.md)
* [Terraform::Linode::Token](Token.md)
* [Terraform::Linode::Volume](Volume.md)