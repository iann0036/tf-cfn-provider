# Terraform::AWS::AthenaDatabase

Provides an Athena database.

## Properties

`Name` - (Required) Name of the database to create.

`Bucket` - (Required) Name of s3 bucket to save the results of the query execution.

`EncryptionConfiguration` - (Optional) The encryption key block AWS Athena uses to decrypt the data in S3, such as an AWS Key Management Service (AWS KMS) key. An `EncryptionConfiguration` block is documented below.

`ForceDestroy` - (Optional, Default: false) A boolean that indicates all tables should be deleted from the database so that the database can be destroyed without error. The tables are *not* recoverable.

`EncryptionOption` - (Required) The type of key; one of `SSE_S3`, `SSE_KMS`, `CSE_KMS`.

`KmsKey` - (Optional) The KMS key ARN or ID; required for key types `SSE_KMS` and `CSE_KMS`.


## Return Values

### Fn::GetAtt

`Id` - The database name.

## See Also

* [aws_athena_database](https://www.terraform.io/docs/providers/aws/r/athena_database.html) in the _Terraform Provider Documentation_