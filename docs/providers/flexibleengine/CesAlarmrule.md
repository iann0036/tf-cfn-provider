# Terraform::FlexibleEngine::CesAlarmrule

Manages a V2 topic resource within FlexibleEngine.

## Properties

`AlarmName` - (Required) Specifies the name of an alarm rule. The value can be a string of 1 to 128 characters that can consist of numbers, lowercase letters, uppercase letters, underscores (_), or hyphens (-).

`AlarmDescription` - (Optional) The value can be a string of 0 to 256 characters.

`Metric` - (Required) Specifies the alarm metrics. The structure is described below.

`Condition` - (Required) Specifies the alarm triggering condition. The structure is described below.

`AlarmActions` - (Optional) Specifies the action list triggered by an alarm. The structure is described below.

`InsufficientdataActions` - (Optional) Specifies the action list triggered by data insufficiency. The structure is described below.

`OkActions` - (Optional) Specifies the action list triggered by the clearing of an alarm. The structure is described below.

`AlarmEnabled` - (Optional) Specifies whether to enable the alarm. The default value is true.

`AlarmActionEnabled` - (Optional) Specifies whether to enable the action to be triggered by an alarm. The default value is true. Note: If alarm_action_enabled is set to true, at least one of the following parameters alarm_actions, insufficientdata_actions, and ok_actions cannot be empty. If alarm_actions, insufficientdata_actions, and ok_actions coexist, their corresponding notification_list must be of the same value.

### Metric Properties

`Namespace` - (Required) Specifies the namespace in service.item format. service.item can be a string of 3 to 32 characters that must start with a letter and can consists of uppercase letters, lowercase letters, numbers, or underscores (_).

`MetricName` - (Required) Specifies the metric name. The value can be a string of 1 to 64 characters that must start with a letter and can consists of uppercase letters, lowercase letters, numbers, or underscores (_).

`Dimensions` - (Required) Specifies the list of metric dimensions. Currently, the maximum length of the dimesion list that are supported is 3. The structure is described below.

### Dimensions Properties

`Name` - (Required) Specifies the dimension name. The value can be a string of 1 to 32 characters that must start with a letter and can consists of uppercase letters, lowercase letters, numbers, underscores (_), or hyphens (-).

`Value` - (Required) Specifies the dimension value. The value can be a string of 1 to 64 characters that must start with a letter or a number and can consists of uppercase letters, lowercase letters, numbers, underscores (_), or hyphens (-).

### Condition Properties

`Period` - (Required) Specifies the alarm checking period in seconds. The value can be 1, 300, 1200, 3600, 14400, and 86400. Note: If period is set to 1, the raw metric data is used to determine whether to generate an alarm.

`Filter` - (Required) Specifies the data rollup methods. The value can be max, min, average, sum, and vaiance.

`ComparisonOperator` - (Required) Specifies the comparison condition of alarm thresholds. The value can be >, =, <, >=, or <=.

`Value` - (Required) Specifies the alarm threshold. The value ranges from 0 to Number of 1.7976931348623157e+308.

`Unit` - (Optional) Specifies the data unit.

`Count` - (Required) Specifies the number of consecutive occurrence times. The value ranges from 1 to 5.

### AlarmActions Properties

`Type` - (Optional) specifies the type of action triggered by an alarm. the value can be notification or autoscaling. notification: indicates that a notification will be sent to the user. autoscaling: indicates that a scaling action will be triggered.

`NotificationList` - (Required) specifies the topic urn list of the target notification objects. the maximum length is 5. the topic urn list can be obtained from simple message notification (smn) and in the following format: urn: smn:([a-z]|[a-z]|[0-9]|\-){1,32}:([a-z]|[a-z]|[0-9]){32}:([a-z]|[a-z]|[0-9]|\-|\_){1,256}. if type is set to notification, the value of notification_list cannot be empty. if type is set to autoscaling, the value of notification_list must be [] and the value of namespace must be sys.as. Note: to enable the as alarm rules take effect, you must bind scaling policies. for details, see the auto scaling api reference.

### InsufficientdataActions Properties

`Type` - (Optional) specifies the type of action triggered by an alarm. the value is notification. notification: indicates that a notification will be sent to the user.

`NotificationList` - (Optional) indicates the list of objects to be notified if the alarm status changes. the maximum length is 5.

### OkActions Properties

`Type` - (Optional) specifies the type of action triggered by an alarm. the value is notification. notification: indicates that a notification will be sent to the user.

`NotificationList` - (Optional) indicates the list of objects to be notified if the alarm status changes. the maximum length is 5.


## Return Values

### Fn::GetAtt

`AlarmName` - See Properties above.

`AlarmDescription` - See Properties above.

`Metric` - See Properties above.

`Condition` - See Properties above.

`AlarmActions` - See Properties above.

`InsufficientdataActions` - See Properties above.

`OkActions` - See Properties above.

`AlarmEnabled` - See Properties above.

`AlarmActionEnabled` - See Properties above.

`Id` - Specifies the alarm rule ID.

`UpdateTime` - Specifies the time when the alarm status changed. The value.

`AlarmState` - Specifies the alarm status. The value can be:.

## See Also

* [flexibleengine_ces_alarmrule](https://www.terraform.io/docs/providers/flexibleengine/r/ces_alarmrule.html) in the _Terraform Provider Documentation_