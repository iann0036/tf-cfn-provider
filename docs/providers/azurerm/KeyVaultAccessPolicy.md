# Terraform::AzureRM::KeyVaultAccessPolicy

Manages a Key Vault Access Policy.

~> **NOTE:** It's possible to define Key Vault Access Policies both within [the `Terraform::AzureRM::KeyVault` resource](keyVault.html) via the `accessPolicy` block and by using [the `azurermKeyVaultAccessPolicy` resource](key_vault_access_policy.html). However it's not possible to use both methods to manage Access Policies within a KeyVault, since there'll be conflicts.

-> **NOTE:** Azure permits a maximum of 16 Access Policies per Key Vault - [more information can be found in this document](https://docs.microsoft.com/en-us/azure/key-vault/key-vault-secure-your-key-vault#data-plane-access-control).

## Properties

`VaultName` - (Required) Specifies the name of the Key Vault resource. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the namespace. Changing this forces a new resource to be created.

`TenantId` - (Required) The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault. Changing this forces a new resource to be created.

`ObjectId` - (Required) The object ID of a user, service principal or security group in the Azure Active Directory tenant for the vault. The object ID must be unique for the list of access policies. Changing this forces a new resource to be created.

`ApplicationId` - (Optional) The object ID of an Application in Azure Active Directory.

`CertificatePermissions` - (Optional) List of certificate permissions, must be one or more from the following: `create`, `delete`, `deleteissuers`, `get`, `getissuers`, `import`, `list`, `listissuers`, `managecontacts`, `manageissuers`, `purge`, `recover`, `setissuers` and `update`.

`KeyPermissions` - (Required) List of key permissions, must be one or more from the following: `backup`, `create`, `decrypt`, `delete`, `encrypt`, `get`, `import`, `list`, `purge`, `recover`, `restore`, `sign`, `unwrapKey`, `update`, `verify` and `wrapKey`.

`SecretPermissions` - (Required) List of secret permissions, must be one or more from the following: `backup`, `delete`, `get`, `list`, `purge`, `recover`, `restore` and `set`.


## Return Values

### Fn::GetAtt

`Id` - Key Vault Access Policy ID.

## See Also

* [azurerm_key_vault_access_policy](https://www.terraform.io/docs/providers/azurerm/r/key_vault_access_policy.html) in the _Terraform Provider Documentation_