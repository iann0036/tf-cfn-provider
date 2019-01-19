# Terraform::AWS::IamAccountPasswordPolicy

-> **Note:** There is only a single policy allowed per AWS account. An existing policy will be lost when using this resource as an effect of this limitation.

Manages Password Policy for the AWS Account.
See more about [Account Password Policy](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html)
in the official AWS docs.

## Properties

`AllowUsersToChangePassword` - (Optional) Whether to allow users to change their own password.

`HardExpiry` - (Optional) Whether users are prevented from setting a new password after their password has expired (i.e. require administrator reset).

`MaxPasswordAge` - (Optional) The number of days that an user password is valid.

`MinimumPasswordLength` - (Optional) Minimum length to require for user passwords.

`PasswordReusePrevention` - (Optional) The number of previous passwords that users are prevented from reusing.

`RequireLowercaseCharacters` - (Optional) Whether to require lowercase characters for user passwords.

`RequireNumbers` - (Optional) Whether to require numbers for user passwords.

`RequireSymbols` - (Optional) Whether to require symbols for user passwords.

`RequireUppercaseCharacters` - (Optional) Whether to require uppercase characters for user passwords.


## Return Values

### Fn::GetAtt

`ExpirePasswords` - Indicates whether passwords in the account expire.

## See Also

* [aws_iam_account_password_policy](https://www.terraform.io/docs/providers/aws/r/iam_account_password_policy.html) in the _Terraform Provider Documentation_