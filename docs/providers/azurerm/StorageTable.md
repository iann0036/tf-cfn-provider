# Terraform::AzureRM::StorageTable

Manage an Azure Storage Table.

## Properties

`Name` - (Required) The name of the storage table. Must be unique within the storage account the table is located.

`ResourceGroupName` - (Required) The name of the resource group in which to
create the storage table. Changing this forces a new resource to be created.

`StorageAccountName` - (Required) Specifies the storage account in which to create the storage table.
Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Storage Table.

## See Also

* [azurerm_storage_table](https://www.terraform.io/docs/providers/azurerm/r/storage_table.html) in the _Terraform Provider Documentation_