# Terraform::AzureRM::RecoveryServicesVault

Manage an Recovery Services Vault.

## Properties

`Name` - (Required) Specifies the name of the Recovery Services Vault. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the Recovery Services Vault. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`Sku` - (Required) Sets the vault's SKU. Possible values include: `Standard`, `RS0`.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Recovery Services Vault.

## See Also

* [azurerm_recovery_services_vault](https://www.terraform.io/docs/providers/azurerm/r/recovery_services_vault.html) in the _Terraform Provider Documentation_