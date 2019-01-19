# Terraform::AzureRM::MonitorLogProfile

Manages a [Log Profile](https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitoring-overview-activity-logs#export-the-activity-log-with-a-log-profile). A Log Profile configures how Activity Logs are exported.

-> **NOTE:** It's only possible to configure one Log Profile per Subscription. If you are trying to create more than one Log Profile, an error with `StatusCode=409` will occur.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The Log Profile resource ID.

## See Also

* [azurerm_monitor_log_profile](https://www.terraform.io/docs/providers/azurerm/r/monitor_log_profile.html) in the _Terraform Provider Documentation_