# Terraform::AzureRM::MonitorMetricAlert

Manages a Metric Alert within Azure Monitor.

## Properties

`ResourceGroupName` - (Required) The name of the resource group in which to create the Metric Alert instance.

`Scopes` - (Required) The resource ID at which the metric criteria should be applied.

`Criteria` - (Required) One or more `Criteria` blocks as defined below.

`Action` - (Optional) One or more `Action` blocks as defined below.

`Enabled` - (Optional) Should this Metric Alert be enabled? Defaults to `true`.

`AutoMitigate` - (Optional) Should the alerts in this Metric Alert be auto resolved? Defaults to `false`.

`Description` - (Optional) The description of this Metric Alert.

`Frequency` - (Optional) The evaluation frequency of this Metric Alert, represented in ISO 8601 duration format. Possible values are `PT1M`, `PT5M`, `PT15M`, `PT30M` and `PT1H`. Defaults to `PT1M`.

`Severity` - (Optional) The severity of this Metric Alert. Possible values are `0`, `1`, `2`, `3` and `4`. Defaults to `3`.

`WindowSize` - (Optional) The period of time that is used to monitor alert activity, represented in ISO 8601 duration format. This value must be greater than `Frequency`. Possible values are `PT1M`, `PT5M`, `PT15M`, `PT30M`, `PT1H`, `PT6H`, `PT12H` and `P1D`. Defaults to `PT5M`.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### Dimension Properties

`Name` - (Required) One of the dimension names.

`Operator` - (Required) The dimension operator. Possible values are `Include` and `Exclude`.

`Values` - (Required) The list of dimension values.

### Action Properties

`ActionGroupId` - (Required) The ID of the Action Group can be sourced from [the `Terraform::AzureRM::MonitorActionGroup` resource](./monitor_action_group.html).

`WebhookProperties` - (Optional) The map of custom string properties to include with the post operation. These data are appended to the webhook payload.

### Criteria Properties

`MetricNamespace` - (Required) One of the metric namespaces to be monitored.

`MetricName` - (Required) One of the metric names to be monitored.

`Aggregation` - (Required) The statistic that runs over the metric values. Possible values are `Average`, `Minimum`, `Maximum` and `Total`.

`Threshold` - (Required) The criteria threshold value that activates the alert.

`Dimension` - (Optional) One or more `Dimension` blocks as defined below.


## Return Values

### Fn::GetAtt

`Id` - The ID of the metric alert.

## See Also

* [azurerm_monitor_metric_alert](https://www.terraform.io/docs/providers/azurerm/r/monitor_metric_alert.html) in the _Terraform Provider Documentation_