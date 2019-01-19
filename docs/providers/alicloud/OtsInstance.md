# Terraform::Alicloud::OtsInstance

This resource will help you to manager a [Table Store](https://www.alibabacloud.com/help/doc-detail/27280.htm) Instance.
It is foundation of creating data table.

## Properties

`Name` - (Required, ForceNew) The name of the instance.

`AccessedBy` - The network limitation of accessing instance. Valid values: * `Any` - Allow all network to access the instance. * `Vpc` - Only can the attached VPC allow to access the instance. * `ConsoleOrVpc` - Allow web console or the attached VPC to access the instance.

`Any` - Allow all network to access the instance. * `Vpc` - Only can the attached VPC allow to access the instance. * `ConsoleOrVpc` - Allow web console or the attached VPC to access the instance.

`Vpc` - Only can the attached VPC allow to access the instance. * `ConsoleOrVpc` - Allow web console or the attached VPC to access the instance.

`ConsoleOrVpc` - Allow web console or the attached VPC to access the instance.

`InstanceType` - (ForceNew) The type of instance. Valid values are "Capacity" and "HighPerformance". Default to "HighPerformance".

`Description` - (Optional, ForceNew) The description of the instance. Currently, it does not support modifying.

`Tags` - A mapping of tags to assign to the instance.


## Return Values

### Fn::GetAtt

`Id` - The resource ID. The value is same as the "name".

`Name` - The instance name.

`Description` - The instance description.

`AccessedBy` - TThe network limitation of accessing instance.

`InstanceType` - The instance type.

`Tags` - The instance tags.

## See Also

* [alicloud_ots_instance](https://www.terraform.io/docs/providers/alicloud/r/ots_instance.html) in the _Terraform Provider Documentation_