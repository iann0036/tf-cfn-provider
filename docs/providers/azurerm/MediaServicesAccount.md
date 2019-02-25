# Terraform::AzureRM::MediaServicesAccount

Manages a Media Services Account.

## Properties

`Name` - (Required) Specifies the name of the Media Services Account. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the Media Services Account. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`StorageAccount` - (Required) One or more `StorageAccount` blocks as defined below.

### StorageAccount Properties

`Id` - (Required) Specifies the ID of the Storage Account that will be associated with the Media Services instance.

`IsPrimary` - (Required) Specifies whether the storage account should be the primary account or not. Defaults to `false`.


## Return Values

### Fn::GetAtt

`Id` - The Resource ID of the Media Services Account.

## See Also

* [azurerm_media_services_account](https://www.terraform.io/docs/providers/azurerm/r/media_services_account.html) in the _Terraform Provider Documentation_