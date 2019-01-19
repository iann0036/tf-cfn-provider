# Terraform::AWS::DmsReplicationTask

Provides a DMS (Data Migration Service) replication task resource. DMS replication tasks can be created, updated, deleted, and imported.

## Properties

`CdcStartTime` - (Optional) The Unix timestamp integer for the start of the Change Data Capture (CDC) operation.

`MigrationType` - (Required) The migration type. Can be one of `full-load | cdc | full-load-and-cdc`.

`ReplicationInstanceArn` - (Required) The Amazon Resource Name (ARN) of the replication instance.

`ReplicationTaskId` - (Required) The replication task identifier.

`ReplicationTaskSettings` - (Optional) An escaped JSON string that contains the task settings. For a complete list of task settings, see [Task Settings for AWS Database Migration Service Tasks](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html).

`SourceEndpointArn` - (Required) The Amazon Resource Name (ARN) string that uniquely identifies the source endpoint.

`TableMappings` - (Required) An escaped JSON string that contains the table mappings. For information on table mapping see [Using Table Mapping with an AWS Database Migration Service Task to Select and Filter Data](http://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.html).

`Tags` - (Optional) A mapping of tags to assign to the resource.

`TargetEndpointArn` - (Required) The Amazon Resource Name (ARN) string that uniquely identifies the target endpoint.


## Return Values

### Fn::GetAtt

`ReplicationTaskArn` - The Amazon Resource Name (ARN) for the replication task.

## See Also

* [aws_dms_replication_task](https://www.terraform.io/docs/providers/aws/r/dms_replication_task.html) in the _Terraform Provider Documentation_