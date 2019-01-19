# Terraform::TencentCloud::CbsSnapshot

Provides a snapshot resource.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The snapshot ID, something looks like `snapshot-xxxxxx`.

`StorageId` - The storage ID which this snapshot created from.

`StorageSize` - The size of assiciated storage. You can create new larger or same size storage use this snapshot.

`SnapshotName` - Name of snapshot.

`Percent` - The creation progress of this snapshot.

`DiskType` - The disk type of this snapshot, `root` or `data`.

`SnapshotStatus` - The status of this snapshot. "creating" means the snapshot is creating; "normal" means the snapshot is ready to use.

## See Also

* [tencentcloud_cbs_snapshot](https://www.terraform.io/docs/providers/tencentcloud/r/cbs_snapshot.html) in the _Terraform Provider Documentation_