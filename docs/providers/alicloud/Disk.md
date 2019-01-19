# Terraform::Alicloud::Disk

Provides a ECS disk resource.

~> **NOTE:** One of `Size` or `SnapshotId` is required when specifying an ECS disk. If all of them be specified, `Size` must more than the size of snapshot which `SnapshotId` represents. Currently, `Terraform::Alicloud::Disk` doesn't resize disk.

## Properties

`AvailabilityZone` - (Required, Forces new resource) The Zone to create the disk in.

`Name` - (Optional) Name of the ECS disk. This name can have a string of 2 to 128 characters, must contain only alphanumeric characters or hyphens, such as "-",".","_", and must not begin or end with a hyphen, and must not begin with http:// or https://. Default value is null.

`Description` - (Optional) Description of the disk. This description can have a string of 2 to 256 characters, It cannot begin with http:// or https://. Default value is null.

`Category` - (Optional, Forces new resource) Category of the disk. Valid values are `cloud`, `cloud_efficiency` and `cloud_ssd`. Default is `cloud_efficiency`.

`Size` - (Required) The size of the disk in GiBs. When resize the disk, the new size must be greater than the former value, or you would get an error `InvalidDiskSize.TooSmall`.

`SnapshotId` - (Optional) A snapshot to base the disk off of. If the disk size required by snapshot is greater than `Size`, the `Size` will be ignored.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`Encrypted` - (Optional) If true, the disk will be encrypted.


## Return Values

### Fn::GetAtt

`Id` - The disk ID.

`AvailabilityZone` - The Zone to create the disk in.

`Name` - The disk name.

`Description` - The disk description.

`Status` - The disk status.

`Category` - The disk category.

`Size` - The disk size.

`SnapshotId` - The disk snapshot ID.

`Tags` - The disk tags.

`Encrypted` - Whether the disk is encrypted.

## See Also

* [alicloud_disk](https://www.terraform.io/docs/providers/alicloud/r/disk.html) in the _Terraform Provider Documentation_