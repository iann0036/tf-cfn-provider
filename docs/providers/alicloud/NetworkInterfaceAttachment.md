# Terraform::Alicloud::NetworkInterfaceAttachment

Provides an Alicloud ECS Elastic Network Interface Attachment as a resource to attach ENI to or detach ENI from ECS Instances.

For information about Elastic Network Interface and how to use it, see [Elastic Network Interface](https://www.alibabacloud.com/help/doc-detail/58496.html).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the resource, formatted as `<network_interface_id>:<instance_id>`.

## See Also

* [alicloud_network_interface_attachment](https://www.terraform.io/docs/providers/alicloud/r/network_interface_attachment.html) in the _Terraform Provider Documentation_