# Terraform::Alicloud::LogtailAttachment

The Logtail access service is a log collection agent provided by Log Service.
You can use Logtail to collect logs from servers such as Alibaba Cloud Elastic
Compute Service (ECS) instances in real time in the Log Service console. [Refer to details](https://www.alibabacloud.com/help/doc-detail/29058.htm)

This resource amis to attach one logtail configure to a machine group.

~> **NOTE:** One logtail configure can be attached to multiple machine groups and one machine group can attach several logtail configures.

## Properties

`Project` - (Required, ForceNew) The project name to the log store belongs.

`LogtailConfigName` - (Required, ForceNew) The Logtail configuration name, which is unique in the same project.

`MachineGroupName` - (Required, ForceNew) The machine group name, which is unique in the same project.


## Return Values

### Fn::GetAtt

`Id` - The ID of the logtail to machine group. It formats of `<project>:<logtail_config_name>:<machine_group_name>`.

## See Also

* [alicloud_logtail_attachment](https://www.terraform.io/docs/providers/alicloud/r/logtail_attachment.html) in the _Terraform Provider Documentation_