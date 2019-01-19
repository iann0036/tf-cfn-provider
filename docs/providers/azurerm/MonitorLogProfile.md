# Terraform::AzureRM::MonitorLogProfile

Manages a [Log Profile](https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitoring-overview-activity-logs#export-the-activity-log-with-a-log-profile). A Log Profile configures how Activity Logs are exported.

-> **NOTE:** It's only possible to configure one Log Profile per Subscription. If you are trying to create more than one Log Profile, an error with `StatusCode=409` will occur.

## Properties

`Name` - (Required) The name of the Log Profile. Changing this forces a new resource to be created.

`Categories` - (Required) List of categories of the logs.

`Locations` - (Required) List of regions for which Activity Log events are stored or streamed.

`StorageAccountId` - (Optional) The resource ID of the storage account in which the Activity Log is stored. At least one of `StorageAccountId` or `ServicebusRuleId` must be set.

`ServicebusRuleId` - (Optional) The service bus (or event hub) rule ID of the service bus (or event hub) namespace in which the Activity Log is streamed to. At least one of `StorageAccountId` or `ServicebusRuleId` must be set.

`RetentionPolicy` - (Required) A `RetentionPolicy` block as documented below. A retention policy for how long Activity Logs are retained in the storage account.

### RetentionPolicy Properties

`Enabled` - (Required) A boolean value to indicate whether the retention policy is enabled.

`Days` - (Optional) The number of days for the retention policy. Defaults to 0.


## Return Values

### Fn::GetAtt

`Id` - The Log Profile resource ID.

## See Also

* [azurerm_monitor_log_profile](https://www.terraform.io/docs/providers/azurerm/r/monitor_log_profile.html) in the _Terraform Provider Documentation_