# Terraform::AWS::IamUserSshKey

Uploads an SSH public key and associates it with the specified IAM user.

## Properties

`Username` - (Required) The name of the IAM user to associate the SSH public key with.

`Encoding` - (Required) Specifies the public key encoding format to use in the response. To retrieve the public key in ssh-rsa format, use `SSH`. To retrieve the public key in PEM format, use `PEM`.

`PublicKey` - (Required) The SSH public key. The public key must be encoded in ssh-rsa format or PEM format.

`Status` - (Optional) The status to assign to the SSH public key. Active means the key can be used for authentication with an AWS CodeCommit repository. Inactive means the key cannot be used. Default is `active`.


## Return Values

### Fn::GetAtt

`SshPublicKeyId` - The unique identifier for the SSH public key.

`Fingerprint` - The MD5 message digest of the SSH public key.

## See Also

* [aws_iam_user_ssh_key](https://www.terraform.io/docs/providers/aws/r/iam_user_ssh_key.html) in the _Terraform Provider Documentation_