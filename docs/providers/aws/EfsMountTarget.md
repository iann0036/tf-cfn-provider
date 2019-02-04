# Terraform::AWS::EfsMountTarget

Provides an Elastic File System (EFS) mount target.

## Properties

`FileSystemId` - (Required) The ID of the file system for which the mount target is intended.

`SubnetId` - (Required) The ID of the subnet to add the mount target in.

`IpAddress` - (Optional) The address (within the address range of the specified subnet) at
which the file system may be mounted via the mount target.

`SecurityGroups` - (Optional) A list of up to 5 VPC security group IDs (that must
be for the same VPC as subnet specified) in effect for the mount target.


## Return Values

### Fn::GetAtt

`Id` - The ID of the mount target.

`DnsName` - The DNS name for the given subnet/AZ per [documented convention](http://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-dns-name.html).

`FileSystemArn` - Amazon Resource Name of the file system.

`NetworkInterfaceId` - The ID of the network interface that Amazon EFS created when it created the mount target.

## See Also

* [aws_efs_mount_target](https://www.terraform.io/docs/providers/aws/r/efs_mount_target.html) in the _Terraform Provider Documentation_