# Terraform::AzureRM::StorageAccount

Manage an Azure Storage Account.

## Properties

`Name` - (Required) Specifies the name of the storage account. Changing this forces a
new resource to be created. This must be unique across the entire Azure service,
not just within the resource group.

`ResourceGroupName` - (Required) The name of the resource group in which to
create the storage account. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the
resource exists. Changing this forces a new resource to be created.

`AccountKind` - (Optional) Defines the Kind of account. Valid options are `Storage`,
`StorageV2` and `BlobStorage`. Changing this forces a new resource to be created.
Defaults to `Storage`.

`AccountTier` - (Required) Defines the Tier to use for this storage account. Valid options are `Standard` and `Premium`. Changing this forces a new resource to be created.

`AccountReplicationType` - (Required) Defines the type of replication to use for this storage account. Valid options are `LRS`, `GRS`, `RAGRS` and `ZRS`.

`AccessTier` - (Optional) Defines the access tier for `BlobStorage` and `StorageV2` accounts. Valid options are `Hot` and `Cool`, defaults to `Hot`.

`EnableBlobEncryption` - (Optional) Boolean flag which controls if Encryption Services are enabled for Blob storage, see [here](https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/) for more information. Defaults to `true`.

`EnableFileEncryption` - (Optional) Boolean flag which controls if Encryption Services are enabled for File storage, see [here](https://azure.microsoft.com/en-us/documentation/articles/storage-service-encryption/) for more information. Defaults to `true`.

`EnableHttpsTrafficOnly` - (Optional) Boolean flag which forces HTTPS if enabled, see [here](https://docs.microsoft.com/en-us/azure/storage/storage-require-secure-transfer/)
for more information.

`AccountEncryptionSource` - (Optional) The Encryption Source for this Storage Account. Possible values are `Microsoft.Keyvault` and `Microsoft.Storage`. Defaults to `Microsoft.Storage`.

`CustomDomain` - (Optional) A `CustomDomain` block as documented below.

`NetworkRules` - (Optional) A `NetworkRules` block as documented below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`Identity` - (Optional) A Managed Service Identity block as defined below.

### CustomDomain Properties

`Name` - (Optional) The Custom Domain Name to use for the Storage Account, which will be validated by Azure.

`UseSubdomain` - (Optional) Should the Custom Domain Name be validated by using indirect CNAME validation?.

### NetworkRules Properties

`Bypass` - (Optional)  Specifies whether traffic is bypassed for Logging/Metrics/AzureServices. Valid options are
any combination of `Logging`, `Metrics`, `AzureServices`, or `None`.

`IpRules` - (Optional) List of IP or IP ranges in CIDR Format. Only IPV4 addresses are allowed.

`VirtualNetworkSubnetIds` - (Optional) A list of resource ids for subnets.

### Identity Properties

`Type` - (Required) Specifies the identity type of the Storage Account. At this time the only allowed value is `SystemAssigned`.


## Return Values

### Fn::GetAtt

`Id` - The storage account Resource ID.

`PrimaryLocation` - The primary location of the storage account.

`SecondaryLocation` - The secondary location of the storage account.

`PrimaryBlobEndpoint` - The endpoint URL for blob storage in the primary location.

`SecondaryBlobEndpoint` - The endpoint URL for blob storage in the secondary location.

`PrimaryQueueEndpoint` - The endpoint URL for queue storage in the primary location.

`SecondaryQueueEndpoint` - The endpoint URL for queue storage in the secondary location.

`PrimaryTableEndpoint` - The endpoint URL for table storage in the primary location.

`SecondaryTableEndpoint` - The endpoint URL for table storage in the secondary location.

`PrimaryFileEndpoint` - The endpoint URL for file storage in the primary location.

`PrimaryAccessKey` - The primary access key for the storage account.

`SecondaryAccessKey` - The secondary access key for the storage account.

`PrimaryConnectionString` - The connection string associated with the primary location.

`SecondaryConnectionString` - The connection string associated with the secondary location.

`PrimaryBlobConnectionString` - The connection string associated with the primary blob location.

`SecondaryBlobConnectionString` - The connection string associated with the secondary blob location.

`Identity` - An `Identity` block as defined below, which contains the Identity information for this Storage Account.

`PrincipalId` - The Principal ID for the Service Principal associated with the Identity of this Storage Account.

`TenantId` - The Tenant ID for the Service Principal associated with the Identity of this Storage Account.

## See Also

* [azurerm_storage_account](https://www.terraform.io/docs/providers/azurerm/r/storage_account.html) in the _Terraform Provider Documentation_