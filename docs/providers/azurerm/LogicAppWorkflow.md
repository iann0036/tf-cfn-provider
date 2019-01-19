# Terraform::AzureRM::LogicAppWorkflow

Manages a Logic App Workflow.

## Properties

`Name` - (Required) Specifies the name of the Logic App Workflow. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the Resource Group in which the Logic App Workflow should be created. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the Logic App Workflow exists. Changing this forces a new resource to be created.

`WorkflowSchema` - (Optional) Specifies the Schema to use for this Logic App Workflow. Defaults to `https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#`. Changing this forces a new resource to be created.

`WorkflowVersion` - (Optional) Specifies the version of the Schema used for this Logic App Workflow. Defaults to `1.0.0.0`. Changing this forces a new resource to be create.d.

`Parameters` - (Optional) A map of Key-Value pairs.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The Logic App Workflow ID.

`AccessEndpoint` - The Access Endpoint for the Logic App Workflow.

## See Also

* [azurerm_logic_app_workflow](https://www.terraform.io/docs/providers/azurerm/r/logic_app_workflow.html) in the _Terraform Provider Documentation_