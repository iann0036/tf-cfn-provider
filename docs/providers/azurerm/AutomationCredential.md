# Terraform::AzureRM::AutomationCredential

Manages a Automation Credential.

## Properties

`Name` - (Required) Specifies the name of the Credential. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which the Credential is created. Changing this forces a new resource to be created.

`AccountName` - (Required) The name of the automation account in which the Credential is created. Changing this forces a new resource to be created.

`Username` - (Required) The username associated with this Automation Credential.

`Password` - (Required) The password associated with this Automation Credential.

`Description` -  (Optional) The description associated with this Automation Credential.


## Return Values

### Fn::GetAtt

`Id` - The Automation Credential ID.

## See Also

* [azurerm_automation_credential](https://www.terraform.io/docs/providers/azurerm/r/automation_credential.html) in the _Terraform Provider Documentation_