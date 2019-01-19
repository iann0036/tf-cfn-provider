# Terraform::AzureRM::AutomationDscNodeconfiguration

Manages a Automation DSC Node Configuration.

## Properties

`Name` - (Required) Specifies the name of the DSC Node Configuration. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which the DSC Node Configuration is created. Changing this forces a new resource to be created.

`AutomationAccountName` - (Required) The name of the automation account in which the DSC Node Configuration is created. Changing this forces a new resource to be created.

`ContentEmbedded` - (Required) The PowerShell DSC Node Configuration (mof content).


## Return Values

### Fn::GetAtt

`Id` - The DSC Node Configuration ID.

## See Also

* [azurerm_automation_dsc_nodeconfiguration](https://www.terraform.io/docs/providers/azurerm/r/automation_dsc_nodeconfiguration.html) in the _Terraform Provider Documentation_