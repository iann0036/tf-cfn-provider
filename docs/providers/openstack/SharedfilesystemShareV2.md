# Terraform::OpenStack::SharedfilesystemShareV2

Use this resource to configure a share.

## Properties

`Name` - (Optional) The name of the share. Changing this updates the name of the existing share.

`Description` - (Optional) The human-readable description for the share. Changing this updates the description of the existing share.

`ShareProto` - (Required) The share protocol - can either be NFS, CIFS, CEPHFS, GLUSTERFS, HDFS or MAPRFS. Changing this creates a new share.

`Size` - (Required) The share size, in GBs. The requested share size cannot be greater than the allowed GB quota. Changing this resizes the existing share.

`ShareType` - (Optional) The share type name. If you omit this parameter, the default share type is used.

`SnapshotId` - (Optional) The UUID of the share's base snapshot. Changing this creates a new share.

`IsPublic` - (Optional) The level of visibility for the share. Set to true to make share public. Set to false to make it private. Default value is false. Changing this updates the existing share.

`Metadata` - (Optional) One or more metadata key and value pairs as a dictionary of strings.

`ShareNetworkId` - (Optional) The UUID of a share network where the share server exists or will be created. If `ShareNetworkId` is not set and you provide a `SnapshotId`, the share_network_id value from the snapshot is used. Changing this creates a new share.

`AvailabilityZone` - (Optional) The share availability zone. Changing this creates a new share.


## Return Values

### Fn::GetAtt

`Id` - The unique ID for the Share.

`Region` - The region in which to obtain the V2 Shared File System client.

`ProjectId` - The owner of the Share.

`Name` - See Properties above.

`Description` - See Properties above.

`ShareProto` - See Properties above.

`Size` - See Properties above.

`ShareType` - See Properties above.

`SnapshotId` - See Properties above.

`IsPublic` - See Properties above.

`Metadata` - See Properties above.

`ShareNetworkId` - See Properties above.

`AvailabilityZone` - See Properties above.

`ExportLocations` - A list of export locations. For example, when a share server.

`HasReplicas` - Indicates whether a share has replicas or not.

`Host` - The share host name.

`ReplicationType` - The share replication type.

`ShareServerId` - The UUID of the share server.

## See Also

* [openstack_sharedfilesystem_share_v2](https://www.terraform.io/docs/providers/openstack/r/sharedfilesystem_share_v2.html) in the _Terraform Provider Documentation_