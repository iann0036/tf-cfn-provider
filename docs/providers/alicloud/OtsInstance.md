# Terraform::Alicloud::OtsInstance

This resource will help you to manager a [Table Store](https://www.alibabacloud.com/help/doc-detail/27280.htm) Instance.
It is foundation of creating data table.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The resource ID. The value is same as the "name".

`Name` - The instance name.

`Description` - The instance description.

`AccessedBy` - TThe network limitation of accessing instance.

`InstanceType` - The instance type.

`Tags` - The instance tags.

## See Also

* [alicloud_ots_instance](https://www.terraform.io/docs/providers/alicloud/r/ots_instance.html) in the _Terraform Provider Documentation_