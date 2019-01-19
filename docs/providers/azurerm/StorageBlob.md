# Terraform::AzureRM::StorageBlob

Manage an Azure Storage Blob.

## Properties

`Name` - (Required) The name of the storage blob. Must be unique within the storage container the blob is located.

`ResourceGroupName` - (Required) The name of the resource group in which to create the storage container. Changing this forces a new resource to be created.

`StorageAccountName` - (Required) Specifies the storage account in which to create the storage container. Changing this forces a new resource to be created.

`StorageContainerName` - (Required) The name of the storage container in which this blob should be created.

`Type` - (Optional) The type of the storage blob to be created. One of either `block` or `page`. When not copying from an existing blob, this becomes required.

`Size` - (Optional) Used only for `page` blobs to specify the size in bytes of the blob to be created. Must be a multiple of 512. Defaults to 0.

`ContentType` - (Optional) The content type of the storage blob. Cannot be defined if `SourceUri` is defined. Defaults to `application/octet-stream`.

`Source` - (Optional) An absolute path to a file on the local system. Cannot be defined if `SourceUri` is defined.

`SourceUri` - (Optional) The URI of an existing blob, or a file in the Azure File service, to use as the source contents for the blob to be created. Changing this forces a new resource to be created. Cannot be defined if `Source` is defined.

`Parallelism` - (Optional) The number of workers per CPU core to run for concurrent uploads. Defaults to `8`.

`Attempts` - (Optional) The number of attempts to make per page or block when uploading. Defaults to `1`.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Storage Blob.

`Url` - The URL of the blob.

## See Also

* [azurerm_storage_blob](https://www.terraform.io/docs/providers/azurerm/r/storage_blob.html) in the _Terraform Provider Documentation_