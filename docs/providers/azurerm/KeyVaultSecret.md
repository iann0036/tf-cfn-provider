# Terraform::AzureRM::KeyVaultSecret

Manages a Key Vault Secret.

~> **Note:** All arguments including the secret value will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The Key Vault Secret ID.

`Version` - The current version of the Key Vault Secret.

## See Also

* [azurerm_key_vault_secret](https://www.terraform.io/docs/providers/azurerm/r/key_vault_secret.html) in the _Terraform Provider Documentation_