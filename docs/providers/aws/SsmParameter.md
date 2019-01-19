# Terraform::AWS::SsmParameter

Provides an SSM Parameter resource.

## Properties

`Name` - (Required) The name of the parameter.

`Type` - (Required) The type of the parameter. Valid types are `String`, `StringList` and `SecureString`.

`Value` - (Required) The value of the parameter.

`Description` - (Optional) The description of the parameter.

`KeyId` - (Optional) The KMS key id or arn for encrypting a SecureString.

`Overwrite` - (Optional) Overwrite an existing parameter. If not specified, will default to `false` if the resource has not been created by terraform to avoid overwrite of existing resource and will default to `true` otherwise (terraform lifecycle rules should then be used to manage the update behavior).

`AllowedPattern` - (Optional) A regular expression used to validate the parameter value.

`Tags` - (Optional) A mapping of tags to assign to the object.


## Return Values

### Fn::GetAtt

`Arn` - The ARN of the parameter.

`Name` - (Required) The name of the parameter.

`Description` - (Required) The description of the parameter.

`Type` - (Required) The type of the parameter. Valid types are `String`, `StringList` and `SecureString`.

`Value` - (Required) The value of the parameter.

## See Also

* [aws_ssm_parameter](https://www.terraform.io/docs/providers/aws/r/ssm_parameter.html) in the _Terraform Provider Documentation_