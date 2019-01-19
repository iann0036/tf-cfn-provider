# CloudScale Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/cloudscale**. The below arguments may be included as the key/value or JSON properties in the secret:

* `token` - (Required) Your cloudscale.ch API token. It can also be specified as a shell environment variable called `CLOUDSCALE_TOKEN`. Please create a cloudscale.ch API token with read/write access in our [Cloud Control Panel](https://control.cloudscale.ch/).


## Supported Resources

* [Terraform::CloudScale::FloatingIp](docs/providers/cloudscale/FloatingIp.md)
* [Terraform::CloudScale::Server](docs/providers/cloudscale/Server.md)