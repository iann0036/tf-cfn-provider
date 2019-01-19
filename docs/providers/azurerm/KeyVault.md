# Terraform::AzureRM::KeyVault

Manages a Key Vault.

~> **NOTE:** It's possible to define Key Vault Access Policies both within [the `azurerm_key_vault` resource](key_vault.html) via the `access_policy` block and by using [the `azurerm_key_vault_access_policy` resource](key_vault_access_policy.html). However it's not possible to use both methods to manage Access Policies within a KeyVault, since there'll be conflicts.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the Key Vault.

`VaultUri` - The URI of the Key Vault, used for performing operations on keys and secrets.

## See Also

* [azurerm_key_vault](https://www.terraform.io/docs/providers/azurerm/r/key_vault.html) in the _Terraform Provider Documentation_