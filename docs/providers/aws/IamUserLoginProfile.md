# Terraform::AWS::IamUserLoginProfile

Provides one-time creation of a IAM user login profile, and uses PGP to
encrypt the password for safe transport to the user. PGP keys can be
obtained from Keybase.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`KeyFingerprint` - The fingerprint of the PGP key used to encrypt.

`EncryptedPassword` - The encrypted password, base64 encoded.

## See Also

* [aws_iam_user_login_profile](https://www.terraform.io/docs/providers/aws/r/iam_user_login_profile.html) in the _Terraform Provider Documentation_