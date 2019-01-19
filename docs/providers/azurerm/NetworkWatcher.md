# Terraform::AzureRM::NetworkWatcher

Manages a Network Watcher.

## Properties

`Name` - (Required) The name of the Network Watcher. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the Network Watcher. Changing this forces a new resource to be created.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The Network Watcher ID.

## See Also

* [azurerm_network_watcher](https://www.terraform.io/docs/providers/azurerm/r/network_watcher.html) in the _Terraform Provider Documentation_