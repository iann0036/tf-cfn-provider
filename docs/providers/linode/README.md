# Linode Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/linode**. The below arguments may be included as the key/value or JSON properties in the secret:

* `token` - (Required) This is your [Linode APIv4 Token](https://developers.linode.com/api/v4#section/Personal-Access-Token).

   The Linode Token can also be specified using the `LINODE_TOKEN` environment variable.


## Supported Resources

* [Terraform::Linode::Domain](docs/providers/linode/Domain.md)
* [Terraform::Linode::Image](docs/providers/linode/Image.md)
* [Terraform::Linode::Instance](docs/providers/linode/Instance.md)
* [Terraform::Linode::NodebalancerConfig](docs/providers/linode/NodebalancerConfig.md)
* [Terraform::Linode::NodebalancerNode](docs/providers/linode/NodebalancerNode.md)
* [Terraform::Linode::Nodebalancer](docs/providers/linode/Nodebalancer.md)
* [Terraform::Linode::Sshkey](docs/providers/linode/Sshkey.md)
* [Terraform::Linode::Stackscript](docs/providers/linode/Stackscript.md)
* [Terraform::Linode::Token](docs/providers/linode/Token.md)
* [Terraform::Linode::Volume](docs/providers/linode/Volume.md)