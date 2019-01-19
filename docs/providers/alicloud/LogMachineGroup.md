# Terraform::Alicloud::LogMachineGroup

Log Service manages all the ECS instances whose logs need to be collected by using the Logtail client in the form of machine groups.
 [Refer to details](https://www.alibabacloud.com/help/doc-detail/28966.htm)

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the log machine group. It formats of `<project>:<name>`.

`Project` - The project name.

`Name` - The machine group name.

`IdentifyType` - The machine identification type.

`IdentifyList` - The machine identification.

`Topic` - The machine group topic.

## See Also

* [alicloud_log_machine_group](https://www.terraform.io/docs/providers/alicloud/r/log_machine_group.html) in the _Terraform Provider Documentation_