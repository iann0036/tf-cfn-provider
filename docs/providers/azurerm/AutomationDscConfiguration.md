# Terraform::AzureRM::AutomationDscConfiguration

Manages a Automation DSC Configuration.

## Properties

`Name` - (Required) Specifies the name of the DSC Configuration. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which the DSC Configuration is created. Changing this forces a new resource to be created.

`AutomationAccountName` - (Required) The name of the automation account in which the DSC Configuration is created. Changing this forces a new resource to be created.

`ContentEmbedded` - (Required) The PowerShell DSC Configuration script.

`Location` - (Required) Must be the same location as the Automation Account.

`LogVerbose` - (Optional) Verbose log option.

`Description` - (Optional) Description to go with DSC Configuration.


## Return Values

### Fn::GetAtt

`Id` - The DSC Configuration ID.

## See Also

* [azurerm_automation_dsc_configuration](https://www.terraform.io/docs/providers/azurerm/r/automation_dsc_configuration.html) in the _Terraform Provider Documentation_