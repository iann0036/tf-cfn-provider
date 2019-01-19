# Terraform::AWS::IamUserSshKey

Uploads an SSH public key and associates it with the specified IAM user.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`SshPublicKeyId` - The unique identifier for the SSH public key.

`Fingerprint` - The MD5 message digest of the SSH public key.

## See Also

* [aws_iam_user_ssh_key](https://www.terraform.io/docs/providers/aws/r/iam_user_ssh_key.html) in the _Terraform Provider Documentation_