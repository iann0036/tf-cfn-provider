# Terraform::AzureRM::AutomationModule

Manages a Automation Module.

## Properties

`Name` - (Required) Specifies the name of the Module. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which the Module is created. Changing this forces a new resource to be created.

`AutomationAccountName` - (Required) The name of the automation account in which the Module is created. Changing this forces a new resource to be created.

`ModuleLink` - (Required) The published Module link.

### ModuleLink Properties

`Uri` - (Required) The uri of the module content (zip or nupkg).


## Return Values

### Fn::GetAtt

`Id` - The Automation Module ID.

## See Also

* [azurerm_automation_module](https://www.terraform.io/docs/providers/azurerm/r/automation_module.html) in the _Terraform Provider Documentation_