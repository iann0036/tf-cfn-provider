# Terraform::TencentCloud::CbsSnapshot

Provides a snapshot resource.

## Properties

`StorageId` - (Required) Source Storage to create this snapshot.

`SnapshotName` - (Optional) The name of the snapshot. This snapshot_name can have a string of 1 to 64 characters. It is supported to modify `SnapshotName` after the snapshot is created.


## Return Values

### Fn::GetAtt

`Id` - The snapshot ID, something looks like `snapshot-xxxxxx`.

`StorageId` - The storage ID which this snapshot created from.

`StorageSize` - The size of assiciated storage. You can create new larger or same size storage use this snapshot.

`SnapshotName` - Name of snapshot.

`Percent` - The creation progress of this snapshot.

`DiskType` - The disk type of this snapshot, `root` or `data`.

`SnapshotStatus` - The status of this snapshot. "creating" means the snapshot is creating; "normal" means the snapshot is ready to use.

## See Also

* [tencentcloud_cbs_snapshot](https://www.terraform.io/docs/providers/tencentcloud/r/cbs_snapshot.html) in the _Terraform Provider Documentation_