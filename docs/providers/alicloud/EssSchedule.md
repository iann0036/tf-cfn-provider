# Terraform::Alicloud::EssSchedule

Provides a ESS schedule resource.

## Properties

`ScheduledAction` - (Required) Operations performed when the scheduled task is triggered. Fill in the unique identifier of the scaling rule.

`LaunchTime` - (Required) Operations performed when the scheduled task is triggered. Fill in the unique identifier of the scaling rule.

`ScheduledTaskName` - (Optional) Display name of the scheduled task, which must be 2-40 characters (English or Chinese) long.

`Description` - (Optional) Description of the scheduled task, which is 2-200 characters (English or Chinese) long.

`LaunchExpirationTime` - (Optional) Time period within which the failed scheduled task is retried. The default value is 600s. Value range: [0, 21600].

`RecurrenceType` - (Optional) Type of the scheduled task to be repeated. RecurrenceType, RecurrenceValue and RecurrenceEndTime must be specified. Optional values:
- Daily: Recurrence interval by day for a scheduled task.
- Weekly: Recurrence interval by week for a scheduled task.
- Monthly: Recurrence interval by month for a scheduled task.

`RecurrenceValue` - (Optional) Value of the scheduled task to be repeated. RecurrenceType, RecurrenceValue and RecurrenceEndTime must be specified.
- Daily: Only one value in the range [1,31] can be filled.
- Weekly: Multiple values can be filled. The values of Sunday to Saturday are 0 to 6 in sequence. Multiple values shall be separated by a comma “,”.
- Monthly: In the format of A-B. The value range of A and B is 1 to 31, and the B value must be greater than the A value.

`RecurrenceEndTime` - (Optional) End time of the scheduled task to be repeated. The date format follows the ISO8601 standard and uses UTC time. It is in the format of YYYY-MM-DDThh:mmZ. A time point 90 days after creation or modification cannot be entered. RecurrenceType, RecurrenceValue and RecurrenceEndTime must be specified.

`TaskEnabled` - (Optional) Whether to enable the scheduled task. The default value is true.


## Return Values

### Fn::GetAtt

`Id` - The schedule task ID.

`ScheduledAction` - The action of schedule task.

`LaunchTime` - The time of schedule task be triggered.

`ScheduledTaskName` - The name of schedule task.

`Description` - The description of schedule task.

`TaskEnabled` - Wether the task is enabled.

## See Also

* [alicloud_ess_schedule](https://www.terraform.io/docs/providers/alicloud/r/ess_schedule.html) in the _Terraform Provider Documentation_