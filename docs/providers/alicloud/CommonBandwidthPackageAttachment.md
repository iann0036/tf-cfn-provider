# Terraform::Alicloud::CommonBandwidthPackageAttachment

Provides an Alicloud Common Bandwidth Package Attachment resource for associating Common Bandwidth Package to EIP Instance.

~> **NOTE:** Terraform will auto build common bandwidth package attachment while it uses `alicloud_common_bandwidth_package_attachment` to build a common bandwidth package attachment resource.

For information about common bandwidth package and how to use it, see [What is Common Bandwidth Package](https://www.alibabacloud.com/help/product/55092.htm).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the common bandwidth package attachment id and formates as `<bandwidth_package_id>:<instance_id>`.

## See Also

* [alicloud_common_bandwidth_package_attachment](https://www.terraform.io/docs/providers/alicloud/r/common_bandwidth_package_attachment.html) in the _Terraform Provider Documentation_