# Terraform::AzureRM::LogAnalyticsWorkspaceLinkedService

Links a Log Analytics (formally Operational Insights) Workspace to another resource. The (currently) only linkable service is an Azure Automation Account.

## Properties

`ResourceGroupName` - (Required) The name of the resource group in which the Log Analytics Linked Service is created. Changing this forces a new resource to be created.

`WorkspaceName` - (Required) Name of the Log Analytics Workspace that will contain the linkedServices resource. Changing this forces a new resource to be created.

`LinkedServiceName` - (Optional) Name of the type of linkedServices resource to connect to the Log Analytics Workspace specified in `WorkspaceName`. Currently it defaults to and only supports `automation` as a value. Changing this forces a new resource to be created.

`LinkedServiceProperties` - (Required) A `LinkedServiceProperties` block as defined below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### LinkedServiceProperties Properties

`ResourceId` - (Required) The resource id of the resource that will be linked to the workspace.


## Return Values

### Fn::GetAtt

`Id` - The Log Analytics Linked Service ID.

`Name` - The automatically generated name of the Linked Service. This cannot be specified. The format is always `<workspace_name>/<linked_service_name>` e.g. `workspace1/Automation`.

## See Also

* [azurerm_log_analytics_workspace_linked_service](https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace_linked_service.html) in the _Terraform Provider Documentation_