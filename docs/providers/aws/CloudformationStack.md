# Terraform::AWS::CloudformationStack

Provides a CloudFormation Stack resource.

## Properties

`Name` - (Required) Stack name.

`TemplateBody` - (Optional) Structure containing the template body (max size: 51,200 bytes).

`TemplateUrl` - (Optional) Location of a file containing the template body (max size: 460,800 bytes).

`Capabilities` - (Optional) A list of capabilities. Valid values: `CAPABILITY_IAM` or `CAPABILITY_NAMED_IAM`.

`DisableRollback` - (Optional) Set to true to disable rollback of the stack if stack creation failed. Conflicts with `OnFailure`.

`NotificationArns` - (Optional) A list of SNS topic ARNs to publish stack related events.

`OnFailure` - (Optional) Action to be taken if stack creation fails. This must be one of: `DO_NOTHING`, `ROLLBACK`, or `DELETE`. Conflicts with `DisableRollback`.

`Parameters` - (Optional) A map of Parameter structures that specify input parameters for the stack.

`PolicyBody` - (Optional) Structure containing the stack policy body. Conflicts w/ `PolicyUrl`.

`PolicyUrl` - (Optional) Location of a file containing the stack policy. Conflicts w/ `PolicyBody`.

`Tags` - (Optional) A list of tags to associate with this stack.

`IamRoleArn` - (Optional) The ARN of an IAM role that AWS CloudFormation assumes to create the stack. If you don't specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.

`TimeoutInMinutes` - (Optional) The amount of time that can pass before the stack status becomes `CREATE_FAILED`.


## Return Values

### Fn::GetAtt

`Id` - A unique identifier of the stack.

`Outputs` - A map of outputs from the stack.

## See Also

* [aws_cloudformation_stack](https://www.terraform.io/docs/providers/aws/r/cloudformation_stack.html) in the _Terraform Provider Documentation_