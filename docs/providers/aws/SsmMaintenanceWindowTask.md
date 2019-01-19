# Terraform::AWS::SsmMaintenanceWindowTask

Provides an SSM Maintenance Window Task resource

## Properties

`WindowId` - (Required) The Id of the maintenance window to register the task with.

`MaxConcurrency` - (Required) The maximum number of targets this task can be run for in parallel.

`MaxErrors` - (Required) The maximum number of errors allowed before this task stops being scheduled.

`TaskType` - (Required) The type of task being registered. The only allowed value is `RUN_COMMAND`.

`TaskArn` - (Required) The ARN of the task to execute.

`ServiceRoleArn` - (Required) The role that should be assumed when executing the task.

`Name` - (Optional) The name of the maintenance window task.

`Description` - (Optional) The description of the maintenance window task.

`Targets` - (Required) The targets (either instances or window target ids). Instances are specified using Key=InstanceIds,Values=instanceid1,instanceid2. Window target ids are specified using Key=WindowTargetIds,Values=window target id1, window target id2.

`Priority` - (Optional) The priority of the task in the Maintenance Window, the lower the number the higher the priority. Tasks in a Maintenance Window are scheduled in priority order with tasks that have the same priority scheduled in parallel.

`LoggingInfo` - (Optional) A structure containing information about an Amazon S3 bucket to write instance-level logs to. Documented below.

`TaskParameters` - (Optional) A structure containing information about parameters required by the particular `TaskArn`. Documented below.

### LoggingInfo Properties

`S3BucketName` - (Required).

`S3Region` - (Required).

`S3BucketPrefix` - (Optional).

### TaskParameters Properties

`Name` - (Required).

`Values` - (Required).


## Return Values

### Fn::GetAtt

`Id` - The ID of the maintenance window task.

## See Also

* [aws_ssm_maintenance_window_task](https://www.terraform.io/docs/providers/aws/r/ssm_maintenance_window_task.html) in the _Terraform Provider Documentation_