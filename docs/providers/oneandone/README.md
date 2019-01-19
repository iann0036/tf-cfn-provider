# 1&1 Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/oneandone**. The below arguments may be included as the key/value or JSON properties in the secret:

* `token` - (Required) If omitted, the `ONEANDONE_TOKEN` environment variable is used.

* `endpoint` - (Optional)

* `retries` - (Optional) Number of retries while waiting for a resource to be provisioned. Default value is 50.


## Supported Resources

* [Terraform::OneAndOne::Baremetal](docs/providers/oneandone/Baremetal.md)
* [Terraform::OneAndOne::BlockStorage](docs/providers/oneandone/BlockStorage.md)
* [Terraform::OneAndOne::Image](docs/providers/oneandone/Image.md)
* [Terraform::OneAndOne::InstanceSize](docs/providers/oneandone/InstanceSize.md)
* [Terraform::OneAndOne::Ip](docs/providers/oneandone/Ip.md)
* [Terraform::OneAndOne::Server](docs/providers/oneandone/Server.md)
* [Terraform::OneAndOne::SshKey](docs/providers/oneandone/SshKey.md)
* [Terraform::OneAndOne::Vpn](docs/providers/oneandone/Vpn.md)