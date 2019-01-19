# Terraform::AWS::StoragegatewayNfsFileShare

Manages an AWS Storage Gateway NFS File Share.

## Properties

`ClientList` - (Required) The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks. Set to `["0.0.0.0/0"]` to not limit access. Minimum 1 item. Maximum 100 items.

`GatewayArn` - (Required) Amazon Resource Name (ARN) of the file gateway.

`LocationArn` - (Required) The ARN of the backed storage used for storing file data.

`RoleArn` - (Required) The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.

`DefaultStorageClass` - (Optional) The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.

`GuessMimeTypeEnabled` - (Optional) Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.

`KmsEncrypted` - (Optional) Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.

`KmsKeyArn` - (Optional) Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `KmsEncrypted` is true.

`NfsFileShareDefaults` - (Optional) Nested argument with file share default values. More information below.

`ObjectAcl` - (Optional) Access Control List permission for S3 bucket objects. Defaults to `private`.

`ReadOnly` - (Optional) Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.

`RequesterPays` - (Optional) Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.

`Squash` - (Optional) Maps a user to anonymous user. Defaults to `RootSquash`. Valid values: `RootSquash` (only root is mapped to anonymous user), `NoSquash` (no one is mapped to anonymous user), `AllSquash` (everyone is mapped to anonymous user).


## See Also

* [aws_storagegateway_nfs_file_share](https://www.terraform.io/docs/providers/aws/r/storagegateway_nfs_file_share.html) in the _Terraform Provider Documentation_