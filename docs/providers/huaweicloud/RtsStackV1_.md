# Terraform::HuaweiCloud::RtsStackV1_

Provides an Huawei Cloud Stack resource.

## Properties

`StackName` - (Required) Specifies the stack name. The value must meet the regular expression rule (^[a-zA-Z][a-zA-Z0-9_.-]{0,254}$). Changing this will create a new stack.

`StackId` - (Required) Specifies the stack UUID.

`Template` - (Optional) Specifies the template. The template content must use the json syntax.

`Environment` - (Optional) Specifies the environment information about the stack.

`Files` - (Optional) Specifies files used in the environment.

`Parameters` - (Optional) Specifies parameter information of the stack.

`TimeoutMins` - (Optional) Specifies the timeout duration.

`TemplateUrl` - (Optional) Specifies the template URL.

`DisableRollback` - (Optional) Specifies whether to perform a rollback if the creation fails.


## Return Values

### Fn::GetAtt

`Outputs` - A map of outputs from the stack.

`Capabilities` - List of stack capabilities for stack.

`NotificationTopics` - List of notification topics for stack.

`Status` - Specifies the stack status.

## See Also

* [huaweicloud_rts_stack_v1_](https://www.terraform.io/docs/providers/huaweicloud/r/rts_stack_v1_.html) in the _Terraform Provider Documentation_