# Terraform::AWS::IotRoleAlias

Provides an IoT role alias.

## Properties

`Alias` - (Required) The name of the role alias.

`RoleArn` - (Required) The identity of the role to which the alias refers.

`CredentialDuration` - (Optional) The duration of the credential, in seconds. If you do not specify a value for this setting, the default maximum of one hour is applied. This setting can have a value from 900 seconds (15 minutes) to 3600 seconds (60 minutes).


## See Also

* [aws_iot_role_alias](https://www.terraform.io/docs/providers/aws/r/iot_role_alias.html) in the _Terraform Provider Documentation_