# 1&1 Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/oneandone**. The below arguments may be included as the key/value or JSON properties in the secret:

* `token` - (Required) If omitted, the `ONEANDONE_TOKEN` environment variable is used.

* `endpoint` - (Optional)

* `retries` - (Optional) Number of retries while waiting for a resource to be provisioned. Default value is 50.


## Supported Resources

* [Terraform::OneAndOne::Baremetal](Baremetal.md)
* [Terraform::OneAndOne::BlockStorage](BlockStorage.md)
* [Terraform::OneAndOne::Image](Image.md)
* [Terraform::OneAndOne::InstanceSize](InstanceSize.md)
* [Terraform::OneAndOne::Ip](Ip.md)
* [Terraform::OneAndOne::Server](Server.md)
* [Terraform::OneAndOne::SshKey](SshKey.md)
* [Terraform::OneAndOne::Vpn](Vpn.md)