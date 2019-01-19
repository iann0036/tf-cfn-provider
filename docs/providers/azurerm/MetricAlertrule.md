# Terraform::AzureRM::MetricAlertrule

Manages a [metric-based alert rule](https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitor-quick-resource-metric-alert-portal) in Azure Monitor.

## Properties

`Name` - (Required) Specifies the name of the alert rule. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the alert rule. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`Description` - (Optional) A verbose description of the alert rule that will be included in the alert email.

`Enabled` - (Optional) If `true`, the alert rule is enabled. Defaults to `true`.

`ResourceId` - (Required) The ID of the resource monitored by the alert rule.

`MetricName` - (Required) The metric that defines what the rule monitors.

`Operator` - (Required) The operator used to compare the metric data and the threshold. Possible values are `GreaterThan`, `GreaterThanOrEqual`, `LessThan`, and `LessThanOrEqual`.

`Threshold` - (Required) The threshold value that activates the alert.

`Period` - (Required) The period of time formatted in [ISO 8601 duration format](https://en.wikipedia.org/wiki/ISO_8601#Durations) that is used to monitor the alert activity based on the threshold. The period must be between 5 minutes and 1 day.

`Aggregation` - (Required) Defines how the metric data is combined over time. Possible values are `Average`, `Minimum`, `Maximum`, `Total`, and `Last`.

`EmailAction` - (Optional) A `EmailAction` block as defined below.

`WebhookAction` - (Optional) A `WebhookAction` block as defined below.

`Tags` - (Optional) A mapping of tags to assign to the resource. Changing this forces a new resource to be created.

### EmailAction Properties

`SendToServiceOwners` - (Optional) If `true`, the administrators (service and co-administrators) of the subscription are notified when the alert is triggered. Defaults to `false`.

`CustomEmails` - (Optional) A list of email addresses to be notified when the alert is triggered.

### WebhookAction Properties

`ServiceUri` - (Required) The service uri of the webhook to POST the notification when the alert is triggered.

`Properties` - (Optional) A dictionary of custom properties to include with the webhook POST operation payload.


## Return Values

### Fn::GetAtt

`Id` - The ID of the alert rule.

## See Also

* [azurerm_metric_alertrule](https://www.terraform.io/docs/providers/azurerm/r/metric_alertrule.html) in the _Terraform Provider Documentation_