# Terraform::AWS::DatasyncTask

Manages an AWS DataSync Task, which represents a configuration for synchronization. Starting an execution of these DataSync Tasks (actually synchronizing files) is performed outside of this Terraform resource.

## Properties

`DestinationLocationArn` - (Required) Amazon Resource Name (ARN) of destination DataSync Location.

`SourceLocationArn` - (Required) Amazon Resource Name (ARN) of source DataSync Location.

`CloudwatchLogGroupArn` - (Optional) Amazon Resource Name (ARN) of the CloudWatch Log Group that is used to monitor and log events in the sync task.

`Name` - (Optional) Name of the DataSync Task.

`Options` - (Optional) Configuration block containing option that controls the default behavior when you start an execution of this DataSync Task. For each individual task execution, you can override these options by specifying an overriding configuration in those executions.

`Tags` - (Optional) Key-value pairs of resource tags to assign to the DataSync Task.


## See Also

* [aws_datasync_task](https://www.terraform.io/docs/providers/aws/r/datasync_task.html) in the _Terraform Provider Documentation_