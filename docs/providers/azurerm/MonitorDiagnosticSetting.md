# Terraform::AzureRM::MonitorDiagnosticSetting

Manages a Diagnostic Setting for an existing Resource.

## Properties

`Name` - (Required) Specifies the name of the Diagnostic Setting. Changing this forces a new resource to be created.

`TargetResourceId` - (Required) The ID of an existing Resource on which to configure Diagnostic Settings. Changing this forces a new resource to be created.

`EventhubName` - (Optional) Specifies the name of the Event Hub where Diagnostics Data should be sent. Changing this forces a new resource to be created.

`EventhubAuthorizationRuleId` - (Optional) Specifies the ID of an Event Hub Namespace Authorization Rule used to send Diagnostics Data. Changing this forces a new resource to be created.

`Log` - (Optional) One or more `Log` blocks as defined below.

`LogAnalyticsWorkspaceId` - (Optional) Specifies the ID of a Log Analytics Workspace where Diagnostics Data should be sent. Changing this forces a new resource to be created.

`Metric` - (Optional) One or more `Metric` blocks as defined below.

`StorageAccountId` - (Optional) With this parameter you can specify a storage account which should be used to send the logs to. Parameter must be a valid Azure Resource ID. Changing this forces a new resource to be created.

### Log Properties

`Category` - (Required) The name of a Diagnostic Log Category for this Resource.

`RetentionPolicy` - (Required) A `RetentionPolicy` block as defined below.

`Enabled` - (Optional) Is this Diagnostic Log enabled? Defaults to `true`.

### Metric Properties

`Category` - (Required) The name of a Diagnostic Metric Category for this Resource.

`RetentionPolicy` - (Required) A `RetentionPolicy` block as defined below.

`Enabled` - (Optional) Is this Diagnostic Metric enabled? Defaults to `true`.

### RetentionPolicy Properties

`Enabled` - (Required) Is this Retention Policy enabled?.

`Days` - (Optional) The number of days for which this Retention Policy should apply.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Diagnostic Setting.

## See Also

* [azurerm_monitor_diagnostic_setting](https://www.terraform.io/docs/providers/azurerm/r/monitor_diagnostic_setting.html) in the _Terraform Provider Documentation_