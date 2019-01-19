# Terraform::Alicloud::CmsAlarm

This resource provides a alarm rule resource and it can be used to monitor several cloud services according different metrics.
Details for [alarm rule](https://www.alibabacloud.com/help/doc-detail/28608.htm).

## Properties

`Name` - (Required) The alarm rule name.

`Project` - (Required, ForceNew) Monitor project name, such as "acs_ecs_dashboard" and "acs_rds_dashboard". For more information, see [Metrics Reference](https://www.alibabacloud.com/help/doc-detail/28619.htm).

`Metric` - (Required, ForceNew) Name of the monitoring metrics corresponding to a project, such as "CPUUtilization" and "networkin_rate". For more information, see [Metrics Reference](https://www.alibabacloud.com/help/doc-detail/28619.htm).

`Dimensions` - (Required, ForceNew) Map of the resources associated with the alarm rule, such as "instanceId", "device" and "port". Each key's value is a string and it uses comma to split multiple items. For more information, see [Metrics Reference](https://www.alibabacloud.com/help/doc-detail/28619.htm).

`Period` - Index query cycle, which must be consistent with that defined for metrics. Default to 300, in seconds.

`Statistics` - Statistical method. It must be consistent with that defined for metrics. Valid values: ["Average", "Minimum", "Maximum"]. Default to "Average".

`Operator` - Alarm comparison operator. Valid values: ["<=", "<", ">", ">=", "==", "!="]. Default to "==".

`Threshold` - (Required) Alarm threshold value, which must be a numeric value currently.

`TriggeredCount` - Number of consecutive times it has been detected that the values exceed the threshold. Default to 3.

`ContactGroups` - (Required) List contact groups of the alarm rule, which must have been created on the console.

`StartTime` - Start time of the alarm effective period. Default to 0 and it indicates the time 00:00. Valid value range: [0, 24].

`EndTime` - End time of the alarm effective period. Default value 24 and it indicates the time 24:00. Valid value range: [0, 24].

`SilenceTime` - Notification silence period in the alarm state, in seconds. Valid value range: [300, 86400]. Default to 86400.

`NotifyType` - Notification type. Valid value [0, 1]. The value 0 indicates TradeManager+email, and the value 1 indicates that TradeManager+email+SMS.

`Enabled` - Whether to enable alarm rule. Default to true.


## Return Values

### Fn::GetAtt

`Id` - The ID of the alarm rule.

`Name` - The alarm name.

`Project` - Monitor project name.

`Metric` - Name of the monitoring metrics.

`Dimensions` - Map of the resources associated with the alarm rule.

`Period` - Index query cycle.

`Statistics` - Statistical method.

`Operator` - Alarm comparison operator.

`Threshold` - Alarm threshold value.

`TriggeredCount` - Number of trigger alarm.

`ContactGroups` - List contact groups of the alarm rule.

`StartTime` - Start time of the alarm effective period.

`EndTime` - End time of the alarm effective period.

`SilenceTime` - Notification silence period in the alarm state.

`NotifyType` - Notification type.

`Enabled` - Whether to enable alarm rule.

`Status` - The current alarm rule status.

## See Also

* [alicloud_cms_alarm](https://www.terraform.io/docs/providers/alicloud/r/cms_alarm.html) in the _Terraform Provider Documentation_