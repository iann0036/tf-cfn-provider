# Terraform::OpenTelekomCloud::RtsStackV1

Provides an OpenTelekomCloud Stack.

## Properties

`Name` - (Required) A unique name for the stack. The value must meet the regular expression rule (`^[a-zA-Z][a-zA-Z0-9_.-]{0,254}$`). Changing this creates a new stack.

`TemplateBody` - (Optional; Required if `TemplateUrl` is empty) Structure containing the template body. The template content must use the yaml syntax.

`TemplateUrl` - (Optional; Required if `TemplateBody` is empty) Location of a file containing the template body.

`Environment` - (Optional) Tthe environment information about the stack.

`Files` - (Optional) Files used in the environment.

`Parameters` - (Optional) A list of Parameter structures that specify input parameters for the stack.

`DisableRollback` - (Optional) Set to true to disable rollback of the stack if stack creation failed.

`TimeoutMins` - (Optional) Specifies the timeout duration.


## Return Values

### Fn::GetAtt

`Outputs` - A map of outputs from the stack.

`Capabilities` - List of stack capabilities for stack.

`NotificationTopics` - List of notification topics for stack.

`Status` - Specifies the stack status.

## See Also

* [opentelekomcloud_rts_stack_v1](https://www.terraform.io/docs/providers/opentelekomcloud/r/rts_stack_v1.html) in the _Terraform Provider Documentation_