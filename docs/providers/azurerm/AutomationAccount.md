# Terraform::AzureRM::AutomationAccount

Manages a Automation Account.

## Properties

`ResourceGroupName` - (Required) The name of the resource group in which the Automation Account is created. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`Sku` - (Required) A `Sku` block as defined below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### Sku Properties

`Name` - (Optional) The SKU name of the account - only `Basic` is supported at this time. Defaults to `Basic`.


## Return Values

### Fn::GetAtt

`Id` - The Automation Account ID.

`DscServerEndpoint` - The DSC Server Endpoint associated with this Automation Account.

`DscPrimaryAccessKey` - The Primary Access Key for the DSC Endpoint associated with this Automation Account.

`DscSecondaryAccessKey` - The Secondary Access Key for the DSC Endpoint associated with this Automation Account.

## See Also

* [azurerm_automation_account](https://www.terraform.io/docs/providers/azurerm/r/automation_account.html) in the _Terraform Provider Documentation_