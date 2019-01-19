# Terraform::AWS::AutoscalingSchedule

Provides an AutoScaling Schedule resource.

## Properties

`AutoscalingGroupName` - (Required) The name or Amazon Resource Name (ARN) of the Auto Scaling group.

`ScheduledActionName` - (Required) The name of this scaling action.

`StartTime` - (Optional) The time for this action to start, in "YYYY-MM-DDThh:mm:ssZ" format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ). If you try to schedule your action in the past, Auto Scaling returns an error message.

`EndTime` - (Optional) The time for this action to end, in "YYYY-MM-DDThh:mm:ssZ" format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ). If you try to schedule your action in the past, Auto Scaling returns an error message.

`Recurrence` - (Optional) The time when recurring future actions will start. Start time is specified by the user following the Unix cron syntax format.

`MinSize` - (Optional) The minimum size for the Auto Scaling group. Default 0. Set to -1 if you don't want to change the minimum size at the scheduled time.

`MaxSize` - (Optional) The maximum size for the Auto Scaling group. Default 0. Set to -1 if you don't want to change the maximum size at the scheduled time.

`DesiredCapacity` - (Optional) The number of EC2 instances that should be running in the group. Default 0.  Set to -1 if you don't want to change the desired capacity at the scheduled time.


## See Also

* [aws_autoscaling_schedule](https://www.terraform.io/docs/providers/aws/r/autoscaling_schedule.html) in the _Terraform Provider Documentation_