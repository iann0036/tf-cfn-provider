# Terraform::Alicloud::CmsAlarm

This resource provides a alarm rule resource and it can be used to monitor several cloud services according different metrics.
Details for [alarm rule](https://www.alibabacloud.com/help/doc-detail/28608.htm).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

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