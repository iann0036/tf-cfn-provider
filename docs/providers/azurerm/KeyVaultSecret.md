# Terraform::AzureRM::KeyVaultSecret

Manages a Key Vault Secret.

~> **Note:** All arguments including the secret value will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Properties

`Name` - (Required) Specifies the name of the Key Vault Secret. Changing this forces a new resource to be created.

`Value` - (Required) Specifies the value of the Key Vault Secret.

`KeyVaultId` - (Required) The ID of the Key Vault where the Secret should be created.

`ContentType` - (Optional) Specifies the content type for the Key Vault Secret.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The Key Vault Secret ID.

`Version` - The current version of the Key Vault Secret.

## See Also

* [azurerm_key_vault_secret](https://www.terraform.io/docs/providers/azurerm/r/key_vault_secret.html) in the _Terraform Provider Documentation_