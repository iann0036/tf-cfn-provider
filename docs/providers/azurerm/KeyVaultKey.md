# Terraform::AzureRM::KeyVaultKey

Manages a Key Vault Key.

## Properties

`Name` - (Required) Specifies the name of the Key Vault Key. Changing this forces a new resource to be created.

`VaultUri` - (Required) Specifies the URI used to access the Key Vault instance, available on the `Terraform::AzureRM::KeyVault` resource.

`KeyType` - (Required) Specifies the Key Type to use for this Key Vault Key. Possible values are `EC` (Elliptic Curve), `Oct` (Octet), `RSA` and `RSA-HSM`. Changing this forces a new resource to be created.

`KeySize` - (Required) Specifies the Size of the Key to create in bytes. For example, 1024 or 2048. Changing this forces a new resource to be created.

`KeyOpts` - (Required) A list of JSON web key operations. Possible values include: `decrypt`, `encrypt`, `sign`, `unwrapKey`, `verify` and `wrapKey`. Please note these values are case sensitive.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The Key Vault Key ID.

`Version` - The current version of the Key Vault Key.

`N` - The RSA modulus of this Key Vault Key.

`E` - The RSA public exponent of this Key Vault Key.

## See Also

* [azurerm_key_vault_key](https://www.terraform.io/docs/providers/azurerm/r/key_vault_key.html) in the _Terraform Provider Documentation_