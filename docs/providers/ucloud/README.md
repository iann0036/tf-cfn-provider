# UCloud Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/ucloud**. The below arguments may be included as the key/value or JSON properties in the secret:

* `public_key` - (Required) This is the UCloud public key.

* `private_key` - (Required) This is the UCloud private key.

* `region` - (Required) This is the UCloud region.

* `project_id` - (Required) This is the UCloud project id.

* `max_retries` - (Optional) This is the max retry attempts number. Default max retry attempts number is `0`.

* `insecure` - (Optional) This is a switch to disable/enable https. (Default: `false`, means enable https).


## Supported Resources

* [Terraform::UCloud::DiskAttachment](DiskAttachment.md)
* [Terraform::UCloud::Disk](Disk.md)
* [Terraform::UCloud::EipAssociation](EipAssociation.md)
* [Terraform::UCloud::Eip](Eip.md)
* [Terraform::UCloud::Instance](Instance.md)
* [Terraform::UCloud::LbAttachment](LbAttachment.md)
* [Terraform::UCloud::LbListener](LbListener.md)
* [Terraform::UCloud::LbRule](LbRule.md)
* [Terraform::UCloud::Lb](Lb.md)
* [Terraform::UCloud::SecurityGroup](SecurityGroup.md)
* [Terraform::UCloud::Subnet](Subnet.md)
* [Terraform::UCloud::UdpnConnection](UdpnConnection.md)
* [Terraform::UCloud::VpcPeeringConnection](VpcPeeringConnection.md)
* [Terraform::UCloud::Vpc](Vpc.md)