# Terraform::AWS::EfsFileSystem

Provides an Elastic File System (EFS) resource.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Arn` - Amazon Resource Name of the file system.

`Id` - The ID that identifies the file system (e.g. fs-ccfc0d65).

`DnsName` - The DNS name for the filesystem per [documented convention](http://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-dns-name.html).

## See Also

* [aws_efs_file_system](https://www.terraform.io/docs/providers/aws/r/efs_file_system.html) in the _Terraform Provider Documentation_