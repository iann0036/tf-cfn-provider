# Terraform::AWS::SsmParameter

Provides an SSM Parameter resource.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Arn` - The ARN of the parameter.

`Name` - (Required) The name of the parameter.

`Description` - (Required) The description of the parameter.

`Type` - (Required) The type of the parameter. Valid types are `String`, `StringList` and `SecureString`.

`Value` - (Required) The value of the parameter.

## See Also

* [aws_ssm_parameter](https://www.terraform.io/docs/providers/aws/r/ssm_parameter.html) in the _Terraform Provider Documentation_