# Terraform::Alicloud::RamLoginProfile

Provides a RAM User Login Profile resource.

## Properties

`UserName` - (Required, Forces new resource) Name of the RAM user. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as "-",".","_", and must not begin with a hyphen.

`Password` - (Required) Password of the RAM user.

`MfaBindRequired` - (Optional) This parameter indicates whether the MFA needs to be bind when the user first logs in. Default value is `false`.

`PasswordResetRequired` - (Optional) This parameter indicates whether the password needs to be reset when the user first logs in. Default value is `false`.


## Return Values

### Fn::GetAtt

`Id` - The login profile ID.

`UserName` - The user name.

`MfaBindRequired` - The parameter which indicates whether the MFA needs to be bind when the user first logs in.

`PasswordResetRequired` - The parameter which indicates whether the password needs to be reset when the user first logs in.

## See Also

* [alicloud_ram_login_profile](https://www.terraform.io/docs/providers/alicloud/r/ram_login_profile.html) in the _Terraform Provider Documentation_