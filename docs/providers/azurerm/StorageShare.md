# Terraform::AzureRM::StorageShare

Manage an Azure Storage File Share.

## Properties

`Name` - (Required) The name of the share. Must be unique within the storage account where the share is located.

`ResourceGroupName` - (Required) The name of the resource group in which to create the share. Changing this forces a new resource to be created.

`StorageAccountName` - (Required) Specifies the storage account in which to create the share. Changing this forces a new resource to be created.

`Quota` - (Optional) The maximum size of the share, in gigabytes. Must be greater than 0, and less than or equal to 5 TB (5120 GB). Default is 5120.


## Return Values

### Fn::GetAtt

`Id` - The storage share Resource ID.

`Url` - The URL of the share.

## See Also

* [azurerm_storage_share](https://www.terraform.io/docs/providers/azurerm/r/storage_share.html) in the _Terraform Provider Documentation_