# Terraform::Alicloud::EssAlarm

Provides a ESS alarm task resource.

## Properties

`Name` - (Optional) The name for ess alarm.

`Description` - (Optional) The description for the alarm.

`AlarmActions` - (Required) The list of actions to execute when this alarm transition into an ALARM state. Each action is specified as ess scaling rule ari.

`ScalingGroupId` - (Required) The scaling group associated with this alarm.

`MetricType` - (Optional) The type for the alarm's associated metric. Supported value: system, custom. "system" means the metric data is collected by Aliyun Cloud Monitor Service(CMS), "custom" means the metric data is upload to CMS by users. Defaults to system.

`MetricName` - (Required) The name for the alarm's associated metric.

`Period` - (Optional) The period in seconds over which the specified statistic is applied. Supported value: 60, 120, 300, 900. Defaults to 300.

`Statistics` - (Optional) The statistic to apply to the alarm's associated metric. Supported value: Average, Minimum, Maximum. Defaults to Average.

`Threshold` - (Required) The value against which the specified statistics is compared.

`ComparisonOperator` - (Optional) The arithmetic operation to use when comparing the specified Statistic and Threshold. The specified Statistic value is used as the first operand. Supported value: >=, <=, >, <. Defaults to >=.

`EvaluationCount` - (Optional) The number of times that needs to satisfies comparison condition before transition into ALARM state. Defaults to 3.

`CloudMonitorGroupId` - (Optional) Defines the application group id defined by CMS which is assigned when you upload custom metric to CMS, only available for custom metirc.

`Dimensions` - (Optional) The dimension map for the alarm's associated metric (documented below). For all metrics, you can not set the dimension key as "scaling_group" or "userId", which is set by default, the second dimension for metric, such as "device" for "PackagesNetIn", need to be set by users.


## See Also

* [alicloud_ess_alarm](https://www.terraform.io/docs/providers/alicloud/r/ess_alarm.html) in the _Terraform Provider Documentation_