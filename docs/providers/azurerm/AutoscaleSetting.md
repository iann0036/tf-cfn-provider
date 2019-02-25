# Terraform::AzureRM::AutoscaleSetting

Manages an AutoScale Setting which can be applied to Virtual Machine Scale Sets, App Services and other scalable resources.

~> **NOTE:** This resource has been deprecated in favour of the `Terraform::AzureRM::MonitorAutoscaleSetting` resource and will be removed in the next major version of the AzureRM Provider. The new resource shares the same fields as this one, and information on migrating across [can be found in this guide](../guides/migrating-between-renamed-resources.html).

## Properties

`Name` - (Required) The name of the AutoScale Setting. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.

`Profile` - (Required) Specifies one or more (up to 20) `Profile` blocks as defined below.

`TargetResourceId` - (Required) Specifies the resource ID of the resource that the autoscale setting should be added to.

`Enabled` - (Optional) Specifies whether automatic scaling is enabled for the target resource. Defaults to `true`.

`Notification` - (Optional) Specifies a `Notification` block as defined below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### Profile Properties

`Name` - (Required) Specifies the name of the profile.

`Capacity` - (Required) A `Capacity` block as defined below.

`Rule` - (Required) One or more (up to 10) `Rule` blocks as defined below.

`FixedDate` - (Optional) A `FixedDate` block as defined below. This cannot be specified if a `Recurrence` block is specified.

`Recurrence` - (Optional) A `Recurrence` block as defined below. This cannot be specified if a `FixedDate` block is specified.

### Capacity Properties

`Default` - (Required) The number of instances that are available for scaling if metrics are not available for evaluation. The default is only used if the current instance count is lower than the default. Valid values are between `0` and `1000`.

`Maximum` - (Required) The maximum number of instances for this resource. Valid values are between `0` and `1000`.

`Minimum` - (Required) The minimum number of instances for this resource. Valid values are between `0` and `1000`.

### Rule Properties

`MetricTrigger` - (Required) A `MetricTrigger` block as defined below.

`ScaleAction` - (Required) A `ScaleAction` block as defined below.

### MetricTrigger Properties

`MetricName` - (Required) The name of the metric that defines what the rule monitors, such as `Percentage CPU` for `Virtual Machine Scale Sets` and `CpuPercentage` for `App Service Plan`.

`MetricResourceId` - (Required) The ID of the Resource which the Rule monitors.

`Operator` - (Required) Specifies the operator used to compare the metric data and threshold. Possible values are: `Equals`, `NotEquals`, `GreaterThan`, `GreaterThanOrEqual`, `LessThan`, `LessThanOrEqual`.

`Statistic` - (Required) Specifies how the metrics from multiple instances are combined. Possible values are `Average`, `Min` and `Max`.

`TimeAggregation` - (Required) Specifies how the data that's collected should be combined over time. Possible values include `Average`, `Count`, `Maximum`, `Minimum`, `Last` and `Total`. Defaults to `Average`.

`TimeGrain` - (Required) Specifies the granularity of metrics that the rule monitors, which must be one of the pre-defined values returned from the metric definitions for the metric. This value must be between 1 minute and 12 hours an be formatted as an ISO 8601 string.

`TimeWindow` - (Required) Specifies the time range for which data is collected, which must be greater than the delay in metric collection (which varies from resource to resource). This value must be between 5 minutes and 12 hours and be formatted as an ISO 8601 string.

`Threshold` - (Required) Specifies the threshold of the metric that triggers the scale action.

### ScaleAction Properties

`Cooldown` - (Required) The amount of time to wait since the last scaling action before this action occurs. Must be between 1 minute and 1 week and formatted as a ISO 8601 string.

`Direction` - (Required) The scale direction. Possible values are `Increase` and `Decrease`.

`Type` - (Required) The type of action that should occur. Possible values are `ChangeCount`, `ExactCount` and `PercentChangeCount`.

`Value` - (Required) The number of instances involved in the scaling action. Defaults to `1`.

### FixedDate Properties

`End` - (Required) Specifies the end date for the profile, formatted as an RFC3339 date string.

`Start` - (Required) Specifies the start date for the profile, formatted as an RFC3339 date string.

### Recurrence Properties

`Timezone` - (Required) The Time Zone used for the `Hours` field. A list of [possible values can be found here](https://msdn.microsoft.com/en-us/library/azure/dn931928.aspx). Defaults to `UTC`.

`Days` - (Required) A list of days that this profile takes effect on. Possible values include `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday` and `Sunday`.

`Hours` - (Required) A list containing a single item, which specifies the Hour interval at which this recurrence should be triggered (in 24-hour time). Possible values are from `0` to `23`.

`Minutes` - (Required) A list containing a single item which specifies the Minute interval at which this recurrence should be triggered.

### Notification Properties

`Email` - (Required) A `Email` block as defined below.

`Webhook` - (Optional) One or more `Webhook` blocks as defined below.

### Email Properties

`SendToSubscriptionAdministrator` - (Optional) Should email notifications be sent to the subscription administrator? Defaults to `false`.

`SendToSubscriptionCoAdministrator` - (Optional) Should email notifications be sent to the subscription co-administrator? Defaults to `false`.

`CustomEmails` - (Optional) Specifies a list of custom email addresses to which the email notifications will be sent.

### Webhook Properties

`ServiceUri` - (Required) The HTTPS URI which should receive scale notifications.

`Properties` - (Optional) A map of settings.


## Return Values

### Fn::GetAtt

`Id` - The ID of the AutoScale Setting.

## See Also

* [azurerm_autoscale_setting](https://www.terraform.io/docs/providers/azurerm/r/autoscale_setting.html) in the _Terraform Provider Documentation_