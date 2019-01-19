# UCloud Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/ucloud**. The below arguments may be included as the key/value or JSON properties in the secret:

* `public_key` - (Required) This is the UCloud public key. It must be provided, but
  it can also be sourced from the `UCLOUD_PUBLIC_KEY` environment variable.

* `private_key` - (Required) This is the UCloud private key. It must be provided, but
  it can also be sourced from the `UCLOUD_PRIVATE_KEY` environment variable.

* `region` - (Required) This is the UCloud region. It must be provided, but
  it can also be sourced from the `UCLOUD_REGION` environment variables.

* `project_id` - (Required) This is the UCloud project id. It must be provided, but
  it can also be sourced from the `UCLOUD_PROJECT_ID` environment variables.

* `max_retries` - (Optional) This is the max retry attempts number. Default max retry attempts number is `0`.

* `insecure` - (Optional) This is a switch to disable/enable https. (Default: `false`, means enable https).


## Supported Resources

* [Terraform::UCloud::DiskAttachment](docs/providers/ucloud/DiskAttachment.md)
* [Terraform::UCloud::Disk](docs/providers/ucloud/Disk.md)
* [Terraform::UCloud::EipAssociation](docs/providers/ucloud/EipAssociation.md)
* [Terraform::UCloud::Eip](docs/providers/ucloud/Eip.md)
* [Terraform::UCloud::Instance](docs/providers/ucloud/Instance.md)
* [Terraform::UCloud::LbAttachment](docs/providers/ucloud/LbAttachment.md)
* [Terraform::UCloud::LbListener](docs/providers/ucloud/LbListener.md)
* [Terraform::UCloud::LbRule](docs/providers/ucloud/LbRule.md)
* [Terraform::UCloud::Lb](docs/providers/ucloud/Lb.md)
* [Terraform::UCloud::SecurityGroup](docs/providers/ucloud/SecurityGroup.md)
* [Terraform::UCloud::Subnet](docs/providers/ucloud/Subnet.md)
* [Terraform::UCloud::UdpnConnection](docs/providers/ucloud/UdpnConnection.md)
* [Terraform::UCloud::VpcPeeringConnection](docs/providers/ucloud/VpcPeeringConnection.md)
* [Terraform::UCloud::Vpc](docs/providers/ucloud/Vpc.md)