# Terraform::AzureStack::StorageAccount

Manages an Azure Storage Account.

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

## See Also

* [azurestack_storage_account](https://www.terraform.io/docs/providers/azurestack/r/storage_account.html) in the _Terraform Provider Documentation_