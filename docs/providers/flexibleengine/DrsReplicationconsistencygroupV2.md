# Terraform::FlexibleEngine::DrsReplicationconsistencygroupV2

Manages a V2 replicationconsistencygroup resource within FlexibleEngine.

## Properties

`Name` - (Optional) The name of the replication consistency group. The name can contain a maximum of 255 bytes.

`Description` - (Optional) The description of the replication consistency group. The description can contain a maximum of 255 bytes.

`ReplicationIds` - (Required) An array of one or more IDs of the EVS replication pairs used to create the replication consistency group.

`PriorityStation` - (Required) The primary AZ of the replication consistency group. That is the AZ where the production disk belongs.

`ReplicationModel` - (Optional) The type of the created replication consistency group. Currently only type hypermetro is supported.


## Return Values

### Fn::GetAtt

`Name` - See Properties above.

`Description` - See Properties above.

`ReplicationIds` - See Properties above.

`PriorityStation` - See Properties above.

`ReplicationModel` - See Properties above.

`Status` - The status of the replication consistency group.

`ReplicationStatus` - The replication status of the replication consistency group.

`CreatedAt` - The creation time of the replication consistency group.

`UpdatedAt` - The update time of the replication consistency group.

`FailureDetail` - The returned error code if the replication consistency group status is error.

`FaultLevel` - The fault level of the replication consistency group.

## See Also

* [flexibleengine_drs_replicationconsistencygroup_v2](https://www.terraform.io/docs/providers/flexibleengine/r/drs_replicationconsistencygroup_v2.html) in the _Terraform Provider Documentation_