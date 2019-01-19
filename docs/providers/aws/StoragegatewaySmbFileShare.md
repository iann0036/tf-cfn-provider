# Terraform::AWS::StoragegatewaySmbFileShare

Manages an AWS Storage Gateway SMB File Share.

## Properties

`GatewayArn` - (Required) Amazon Resource Name (ARN) of the file gateway.

`LocationArn` - (Required) The ARN of the backed storage used for storing file data.

`RoleArn` - (Required) The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.

`Authentication` - (Optional) The authentication method that users use to access the file share. Defaults to `ActiveDirectory`. Valid values: `ActiveDirectory`, `GuestAccess`.

`DefaultStorageClass` - (Optional) The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.

`GuessMimeTypeEnabled` - (Optional) Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.

`InvalidUserList` - (Optional) A list of users in the Active Directory that are not allowed to access the file share. Only valid if `Authentication` is set to `ActiveDirectory`.

`KmsEncrypted` - (Optional) Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.

`KmsKeyArn` - (Optional) Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `KmsEncrypted` is true.

`SmbFileShareDefaults` - (Optional) Nested argument with file share default values. More information below.

`ObjectAcl` - (Optional) Access Control List permission for S3 bucket objects. Defaults to `private`.

`ReadOnly` - (Optional) Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.

`RequesterPays` - (Optional) Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.

`ValidUserList` - (Optional) A list of users in the Active Directory that are allowed to access the file share. Only valid if `Authentication` is set to `ActiveDirectory`.


## See Also

* [aws_storagegateway_smb_file_share](https://www.terraform.io/docs/providers/aws/r/storagegateway_smb_file_share.html) in the _Terraform Provider Documentation_