# Terraform::AWS::NeptuneParameterGroup

Manages a Neptune Parameter Group

## Properties

`Name` - (Required) The name of the Neptune parameter.

`Family` - (Required) The family of the Neptune parameter group.

`Description` - (Optional) The description of the Neptune parameter group. Defaults to "Managed by Terraform".

`Parameter` - (Optional) A list of Neptune parameters to apply.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`Value` - (Required) The value of the Neptune parameter.

`ApplyMethod` - (Optional) The apply method of the Neptune parameter. Valid values are `immediate` and `pending-reboot`. Defaults to `pending-reboot`.


## Return Values

### Fn::GetAtt

`Id` - The Neptune parameter group name.

`Arn` - The Neptune parameter group Amazon Resource Name (ARN).

## See Also

* [aws_neptune_parameter_group](https://www.terraform.io/docs/providers/aws/r/neptune_parameter_group.html) in the _Terraform Provider Documentation_