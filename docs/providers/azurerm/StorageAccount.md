# Terraform::AzureRM::StorageAccount

Manage an Azure Storage Account.

## Properties

TBC

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

`Identity` - An `identity` block as defined below, which contains the Identity information for this Storage Account.

`PrincipalId` - The Principal ID for the Service Principal associated with the Identity of this Storage Account.

`TenantId` - The Tenant ID for the Service Principal associated with the Identity of this Storage Account.

## See Also

* [azurerm_storage_account](https://www.terraform.io/docs/providers/azurerm/r/storage_account.html) in the _Terraform Provider Documentation_