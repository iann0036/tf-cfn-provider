# Terraform::AzureRM::KeyVault

Manages a Key Vault.

~> **NOTE:** It's possible to define Key Vault Access Policies both within [the `Terraform::AzureRM::KeyVault` resource](keyVault.html) via the `AccessPolicy` block and by using [the `azurermKeyVaultAccessPolicy` resource](key_vault_access_policy.html). However it's not possible to use both methods to manage Access Policies within a KeyVault, since there'll be conflicts.

## Properties

`Name` - (Required) Specifies the name of the Key Vault. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the Key Vault. Changing this forces a new resource to be created.

`Sku` - (Required) An SKU block as described below.

`TenantId` - (Required) The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault.

`AccessPolicy` - (Optional) An access policy block as described below. A maximum of 16 may be declared.

`EnabledForDeployment` - (Optional) Boolean flag to specify whether Azure Virtual Machines are permitted to retrieve certificates stored as secrets from the key vault. Defaults to `false`.

`EnabledForDiskEncryption` - (Optional) Boolean flag to specify whether Azure Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys. Defaults to `false`.

`EnabledForTemplateDeployment` - (Optional) Boolean flag to specify whether Azure Resource Manager is permitted to retrieve secrets from the key vault. Defaults to `false`.

`NetworkAcls` - (Optional) A `NetworkAcls` block as defined below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### AccessPolicy Properties

`TenantId` - (Required) The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault. Must match the `TenantId` used above.

`ObjectId` - (Required) The object ID of a user, service principal or security group in the Azure Active Directory tenant for the vault. The object ID must be unique for the list of access policies.

`ApplicationId` - (Optional) The object ID of an Application in Azure Active Directory.

`CertificatePermissions` - (Optional) List of certificate permissions, must be one or more from the following: `backup`, `create`, `delete`, `deleteissuers`, `get`, `getissuers`, `import`, `list`, `listissuers`, `managecontacts`, `manageissuers`, `purge`, `recover`, `restore`, `setissuers` and `update`.

`KeyPermissions` - (Required) List of key permissions, must be one or more from the following: `backup`, `create`, `decrypt`, `delete`, `encrypt`, `get`, `import`, `list`, `purge`, `recover`, `restore`, `sign`, `unwrapKey`, `update`, `verify` and `wrapKey`.

`SecretPermissions` - (Required) List of secret permissions, must be one or more from the following: `backup`, `delete`, `get`, `list`, `purge`, `recover`, `restore` and `set`.

### NetworkAcls Properties

`Bypass` - (Required) Specifies which traffic can bypass the network rules. Possible values are `AzureServices` and `None`.

`DefaultAction` - (Required) The Default Action to use when no rules match from `IpRules` / `VirtualNetworkSubnetIds`. Possible values are `Allow` and `Deny`.

`IpRules` - (Optional) One or more IP Addresses, or CIDR Blocks which should be able to access thie Key Vault.

`VirtualNetworkSubnetIds` - (Optional) One or more Subnet ID's which should be able to access this Key Vault.

### Sku Properties

`Name` - (Required) The Name of the SKU used for this Key Vault. Possible values are `standard` and `premium`.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Key Vault.

`VaultUri` - The URI of the Key Vault, used for performing operations on keys and secrets.

## See Also

* [azurerm_key_vault](https://www.terraform.io/docs/providers/azurerm/r/key_vault.html) in the _Terraform Provider Documentation_