# Terraform::AWS::EfsMountTarget

Provides an Elastic File System (EFS) mount target.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the mount target.

`DnsName` - The DNS name for the given subnet/AZ per [documented convention](http://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-dns-name.html).

`FileSystemArn` - Amazon Resource Name of the file system.

`NetworkInterfaceId` - The ID of the network interface that Amazon EFS created when it created the mount target.

## See Also

* [aws_efs_mount_target](https://www.terraform.io/docs/providers/aws/r/efs_mount_target.html) in the _Terraform Provider Documentation_