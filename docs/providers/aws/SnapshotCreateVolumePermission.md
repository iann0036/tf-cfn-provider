# Terraform::AWS::SnapshotCreateVolumePermission

Adds permission to create volumes off of a given EBS Snapshot.

## Properties

`SnapshotId` - (required) A snapshot ID.

`AccountId` - (required) An AWS Account ID to add create volume permissions.


## Return Values

### Fn::GetAtt

`Id` - A combination of "`SnapshotId`-`AccountId`".

## See Also

* [aws_snapshot_create_volume_permission](https://www.terraform.io/docs/providers/aws/r/snapshot_create_volume_permission.html) in the _Terraform Provider Documentation_