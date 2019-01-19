# Terraform::AWS::IamAccessKey

Provides an IAM access key. This is a set of credentials that allow API requests to be made as an IAM user.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The access key ID.

`User` - The IAM user associated with this access key.

`KeyFingerprint` - The fingerprint of the PGP key used to encrypt.

`Secret` - The secret access key. Note that this will be written.

`EncryptedSecret` - The encrypted secret, base64 encoded.

`SesSmtpPassword` - The secret access key converted into an SES SMTP.

`Status` - "Active" or "Inactive". Keys are initially active, but can be made.

## See Also

* [aws_iam_access_key](https://www.terraform.io/docs/providers/aws/r/iam_access_key.html) in the _Terraform Provider Documentation_