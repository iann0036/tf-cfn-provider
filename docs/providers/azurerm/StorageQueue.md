# Terraform::AzureRM::StorageQueue

Manage an Azure Storage Queue.

## Properties

`Name` - (Required) The name of the storage queue. Must be unique within the storage account the queue is located.

`ResourceGroupName` - (Required) The name of the resource group in which to
create the storage queue. Changing this forces a new resource to be created.

`StorageAccountName` - (Required) Specifies the storage account in which to create the storage queue.
Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Storage Queue.

## See Also

* [azurerm_storage_queue](https://www.terraform.io/docs/providers/azurerm/r/storage_queue.html) in the _Terraform Provider Documentation_