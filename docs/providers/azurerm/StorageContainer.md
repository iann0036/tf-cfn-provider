# Terraform::AzureRM::StorageContainer

Manage an Azure Storage Container.

## Properties

`Name` - (Required) The name of the storage container. Must be unique within the storage service the container is located.

`ResourceGroupName` - (Required) The name of the resource group in which to
create the storage container. Changing this forces a new resource to be created.

`StorageAccountName` - (Required) Specifies the storage account in which to create the storage container.
Changing this forces a new resource to be created.

`ContainerAccessType` - (Optional) The 'interface' for access the container provides. Can be either `blob`, `container` or `private`. Defaults to `private`.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Storage Container.

`Properties` - Key-value definition of additional properties associated to the storage container.

## See Also

* [azurerm_storage_container](https://www.terraform.io/docs/providers/azurerm/r/storage_container.html) in the _Terraform Provider Documentation_