# Terraform::FlexibleEngine::DrsReplicationV2

Manages a V2 replication resource within FlexibleEngine.

## Properties

`Name` - (Optional) The name of the EVS replication pair. The name can contain a maximum of 255 bytes.

`Description` - (Optional) The description of the EVS replication pair. The description can contain a maximum of 255 bytes.

`VolumeIds` - (Required) An array of one or more IDs of the EVS disks used to create the EVS replication pair.

`PriorityStation` - (Required) The primary AZ of the EVS replication pair. That is the AZ where the production disk belongs.

`ReplicationModel` - (Optional) The type of the EVS replication pair. Currently only type hypermetro is supported.


## Return Values

### Fn::GetAtt

`Name` - See Properties above.

`Description` - See Properties above.

`VolumeIds` - See Properties above.

`PriorityStation` - See Properties above.

`ReplicationModel` - See Properties above.

`Status` - The status of the EVS replication pair.

`ReplicationConsistencyGroupId` - The ID of the replication consistency group where the EVS replication pair belongs.

`CreatedAt` - The creation time of the EVS replication pair.

`UpdatedAt` - The update time of the EVS replication pair.

`ReplicationStatus` - The replication status of the EVS replication pair.

`Progress` - The synchronization progress of the EVS replication pair. Unit: %.

`FailureDetail` - The returned error code if the EVS replication pair status is error.

`RecordMetadata` - The metadata of the EVS replication pair.

`FaultLevel` - The fault level of the EVS replication pair.

## See Also

* [flexibleengine_drs_replication_v2](https://www.terraform.io/docs/providers/flexibleengine/r/drs_replication_v2.html) in the _Terraform Provider Documentation_