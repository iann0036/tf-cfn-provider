# Terraform::AzureRM::ContainerRegistry

Manages an Azure Container Registry.

~> **Note:** All arguments including the access key will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The Container Registry ID.

`LoginServer` - The URL that can be used to log into the container registry.

`AdminUsername` - The Username associated with the Container Registry Admin account - if the admin account is enabled.

`AdminPassword` - The Password associated with the Container Registry Admin account - if the admin account is enabled.

## See Also

* [azurerm_container_registry](https://www.terraform.io/docs/providers/azurerm/r/container_registry.html) in the _Terraform Provider Documentation_