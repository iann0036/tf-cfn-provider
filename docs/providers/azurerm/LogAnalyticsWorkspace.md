# Terraform::AzureRM::LogAnalyticsWorkspace

Manages a Log Analytics (formally Operational Insights) Workspace.

## Properties

`Name` - (Required) Specifies the name of the Log Analytics Workspace. Workspace name should include 4-63 letters, digits or '-'. The '-' shouldn't be the first or the last symbol. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which the Log Analytics workspace is created. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`Sku` - (Required) Specifies the Sku of the Log Analytics Workspace. Possible values are `Free`, `PerNode`, `Premium`, `Standard`, `Standalone`, `Unlimited`, and `PerGB2018` (new Sku as of `2018-04-03`).

`RetentionInDays` - (Optional) The workspace data retention in days. Possible values range between 30 and 730.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The Log Analytics Workspace ID.

`PrimarySharedKey` - The Primary shared key for the Log Analytics Workspace.

`SecondarySharedKey` - The Secondary shared key for the Log Analytics Workspace.

`WorkspaceId` - The Workspace (or Customer) ID for the Log Analytics Workspace.

`PortalUrl` - The Portal URL for the Log Analytics Workspace.

## See Also

* [azurerm_log_analytics_workspace](https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace.html) in the _Terraform Provider Documentation_