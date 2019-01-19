# Terraform::AzureRM::DatabricksWorkspace

Manages a Databricks Workspace

## Properties

`Name` - (Required) Specifies the name of the Databricks Workspace resource. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the Resource Group in which the Databricks Workspace should exist. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource has to be created. Changing this forces a new resource to be created.

`Sku` - (Required) The `Sku` to use for the Databricks Workspace. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.

`ManagedResourceGroupName` - (Optional) The name of the resource group where Azure should place the managed Databricks resources. Changing this forces a new resource to be created.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Databricks Workspace.

`ManagedResourceGroupId` - The ID of the Managed Resource Group created by the Databricks Workspace.

## See Also

* [azurerm_databricks_workspace](https://www.terraform.io/docs/providers/azurerm/r/databricks_workspace.html) in the _Terraform Provider Documentation_