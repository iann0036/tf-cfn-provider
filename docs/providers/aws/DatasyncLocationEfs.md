# Terraform::AWS::DatasyncLocationEfs

Manages an AWS DataSync EFS Location.

~> **NOTE:** The EFS File System must have a mounted EFS Mount Target before creating this resource.

## Properties

`Ec2Config` - (Required) Configuration block containing EC2 configurations for connecting to the EFS File System.

`EfsFileSystemArn` - (Required) Amazon Resource Name (ARN) of EFS File System.

`Subdirectory` - (Optional) Subdirectory to perform actions as source or destination. Default `/`.

`Tags` - (Optional) Key-value pairs of resource tags to assign to the DataSync Location.


## See Also

* [aws_datasync_location_efs](https://www.terraform.io/docs/providers/aws/r/datasync_location_efs.html) in the _Terraform Provider Documentation_