# Terraform::AzureRM::SearchService

Allows you to manage an Azure Search Service.

## Properties

`Name` - (Required) The name of the Search Service. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the Search Service. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`Sku` - (Required) Valid values are `free` and `standard`. `standard2` and `standard3` are also valid, but can only be used when it's enabled on the backend by Microsoft support. `free` provisions the service in shared clusters. `standard` provisions the service in dedicated clusters.  Changing this forces a new resource to be created.

`ReplicaCount` - (Optional) Default is 1. Valid values include 1 through 12. Valid only when `Sku` is `standard`. Changing this forces a new resource to be created.

`PartitionCount` - (Optional) Default is 1. Valid values include 1, 2, 3, 4, 6, or 12. Valid only when `Sku` is `standard`. Changing this forces a new resource to be created.

`Tags` - (Optional) A mapping of tags to assign to the resource. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The Search Service ID.

`PrimaryKey` - The Search Service Administration primary key.

`SecondaryKey` - The Search Service Administration secondary key.

## See Also

* [azurerm_search_service](https://www.terraform.io/docs/providers/azurerm/r/search_service.html) in the _Terraform Provider Documentation_