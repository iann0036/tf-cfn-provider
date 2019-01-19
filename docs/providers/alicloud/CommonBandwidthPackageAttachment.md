# Terraform::Alicloud::CommonBandwidthPackageAttachment

Provides an Alicloud Common Bandwidth Package Attachment resource for associating Common Bandwidth Package to EIP Instance.

~> **NOTE:** Terraform will auto build common bandwidth package attachment while it uses `Terraform::Alicloud::CommonBandwidthPackageAttachment` to build a common bandwidth package attachment resource.

For information about common bandwidth package and how to use it, see [What is Common Bandwidth Package](https://www.alibabacloud.com/help/product/55092.htm).

## Properties

`BandwidthPackageId` - (Required, ForceNew) The bandwidth_package_id of the common bandwidth package attachment, the field can't be changed.

`InstanceId` - (Required, ForceNew) The instance_id of the common bandwidth package attachment, the field can't be changed.


## Return Values

### Fn::GetAtt

`Id` - The ID of the common bandwidth package attachment id and formates as `<bandwidth_package_id>:<instance_id>`.

## See Also

* [alicloud_common_bandwidth_package_attachment](https://www.terraform.io/docs/providers/alicloud/r/common_bandwidth_package_attachment.html) in the _Terraform Provider Documentation_