# Terraform::AzureStack::StorageAccount

Manages an Azure Storage Account.

## Properties

`Name` - (Optional) The Custom Domain Name to use for the Storage Account, which will be validated by Azure.

`ResourceGroupName` - (Required) The name of the resource group in which to create the storage account. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`AccountKind` - (Optional) Defines the Kind of account. Valid option is `Storage`. . Changing this forces a new resource to be created. Defaults to `Storage` currently as per [Azure Stack Storage Differences](https://docs.microsoft.com/en-us/azure/azure-stack/user/azure-stack-acs-differences).

`AccountTier` - (Required) Defines the Tier to use for this storage account. Valid options are `Standard` and `Premium`. Changing this forces a new resource to be created - **`Can be provisioned, but no performance limit or guarantee.`**.

`AccountReplicationType` - (Required) Defines the type of replication to use for this storage account. Valid option is `LRS` currently as per [Azure Stack Storage Differences](https://docs.microsoft.com/en-us/azure/azure-stack/user/azure-stack-acs-differences).

`AccessTier` - (Required for `BlobStorage` accounts) Defines the access tier for `BlobStorage` accounts. Valid options are `Hot` and `Cold`, defaults to `Hot`. - **`Currently Not Supported on Azure Stack`**.

`AccountEncryptionSource` - (Optional) The Encryption Source for this Storage Account. Possible values are `Microsoft.Keyvault` and `Microsoft.Storage`. Defaults to `Microsoft.Storage`.

`CustomDomain` - (Optional) A `CustomDomain` block as documented below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`UseSubdomain` - (Optional) Should the Custom Domain Name be validated by using indirect CNAME validation?.


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