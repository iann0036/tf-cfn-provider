# Terraform::AWS::IamUserLoginProfile

Provides one-time creation of a IAM user login profile, and uses PGP to
encrypt the password for safe transport to the user. PGP keys can be
obtained from Keybase.

## Properties

`User` - (Required) The IAM user's name.

`PgpKey` - (Required) Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:username`.

`PasswordResetRequired` - (Optional, default "true") Whether the user should be forced to reset the generated password on first login.

`PasswordLength` - (Optional, default 20) The length of the generated password.


## Return Values

### Fn::GetAtt

`KeyFingerprint` - The fingerprint of the PGP key used to encrypt.

`EncryptedPassword` - The encrypted password, base64 encoded.

## See Also

* [aws_iam_user_login_profile](https://www.terraform.io/docs/providers/aws/r/iam_user_login_profile.html) in the _Terraform Provider Documentation_