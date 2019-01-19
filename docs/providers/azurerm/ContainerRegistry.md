# Terraform::AzureRM::ContainerRegistry

Manages an Azure Container Registry.

~> **Note:** All arguments including the access key will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Properties

`Name` - (Required) Specifies the name of the Container Registry. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the Container Registry. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`AdminEnabled` - (Optional) Specifies whether the admin user is enabled. Defaults to `false`.

`StorageAccountId` - (Required for `Classic` Sku - Optional otherwise) The ID of a Storage Account which must be located in the same Azure Region as the Container Registry.

`Sku` - (Optional) The SKU name of the the container registry. Possible values are `Classic` (which was previously `Basic`), `Basic`, `Standard` and `Premium`.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`GeoreplicationLocations` - (Optional) A list of Azure locations where the container registry should be geo-replicated.


## Return Values

### Fn::GetAtt

`Id` - The Container Registry ID.

`LoginServer` - The URL that can be used to log into the container registry.

`AdminUsername` - The Username associated with the Container Registry Admin account - if the admin account is enabled.

`AdminPassword` - The Password associated with the Container Registry Admin account - if the admin account is enabled.

## See Also

* [azurerm_container_registry](https://www.terraform.io/docs/providers/azurerm/r/container_registry.html) in the _Terraform Provider Documentation_