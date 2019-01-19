# Terraform::Alicloud::LogMachineGroup

Log Service manages all the ECS instances whose logs need to be collected by using the Logtail client in the form of machine groups.
 [Refer to details](https://www.alibabacloud.com/help/doc-detail/28966.htm)

## Properties

`Project` - (Required, ForceNew) The project name to the machine group belongs.

`Name` - (Required, ForceNew) The machine group name, which is unique in the same project.

`IdentifyType` - The machine identification type, including IP and user-defined identity. Valid values are "ip" and "userdefined". Default to "ip".

`IdentifyList` -  The specific machine identification, which can be an IP address or user-defined identity.

`Topic` - The topic of a machine group.


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