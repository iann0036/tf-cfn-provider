# Terraform::AzureRM::LogAnalyticsSolution

Manages a Log Analytics (formally Operational Insights) Solution.

## Properties

`SolutionName` - (Required) Specifies the name of the solution to be deployed. See [here for options](https://docs.microsoft.com/en-us/azure/log-analytics/log-analytics-add-solutions).Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which the Log Analytics solution is created. Changing this forces a new resource to be created. Note: The solution and it's related workspace can only exist in the same resource group.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`WorkspaceResourceId` - (Required) The full resource ID of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.

`WorkspaceName` - (Required) The full name of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.

`Plan` - (Required) A `Plan` block as documented below.

`Publisher` - (Required) The publisher of the solution. For example `Microsoft`. Changing this forces a new resource to be created.

`Product` - (Required) The product name of the solution. For example `OMSGallery/Containers`. Changing this forces a new resource to be created.

`PromotionCode` - (Optional) A promotion code to be used with the solution.


## See Also

* [azurerm_log_analytics_solution](https://www.terraform.io/docs/providers/azurerm/r/log_analytics_solution.html) in the _Terraform Provider Documentation_