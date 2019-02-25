# CloudScale Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/cloudscale** or add [template metadata](https://github.com/iann0036/tf-cfn-provider/blob/master/examples/metadata.yaml). The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `token` - (Required) Your cloudscale.ch API token. Please create a cloudscale.ch API token with read/write access in our [Cloud Control Panel](https://control.cloudscale.ch/).


## Supported Resources

* [Terraform::CloudScale::FloatingIp](FloatingIp.md)
* [Terraform::CloudScale::Server](Server.md)