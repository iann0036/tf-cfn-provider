# Terraform::Alicloud::Disk

Provides a ECS disk resource.

~> **NOTE:** One of `size` or `snapshot_id` is required when specifying an ECS disk. If all of them be specified, `size` must more than the size of snapshot which `snapshot_id` represents. Currently, `alicloud_disk` doesn't resize disk.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

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