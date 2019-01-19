# Terraform::AzureRM::DevTestVirtualNetwork

Manages a Virtual Network within a Dev Test Lab.

## Properties

`Name` - (Required) Specifies the name of the Dev Test Virtual Network. Changing this forces a new resource to be created.

`LabName` - (Required) Specifies the name of the Dev Test Lab in which the Virtual Network should be created. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which the Dev Test Lab resource exists. Changing this forces a new resource to be created.

`Description` - (Optional) A description for the Virtual Network.

`Subnet` - (Optional) A `Subnet` block as defined below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`UsePublicIpAddress` - (Required) Can Virtual Machines in this Subnet use Public IP Addresses? Possible values are `Allow`, `Default` and `Deny`.

`UseInVirtualMachineCreation` - (Required) Can this subnet be used for creating Virtual Machines? Possible values are `Allow`, `Default` and `Deny`.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Dev Test Virtual Network.

`Subnet` - A `Subnet` block as defined below.

`UniqueIdentifier` - The unique immutable identifier of the Dev Test Virtual Network.

`Name` - The name of the Subnet for this Virtual Network.

## See Also

* [azurerm_dev_test_virtual_network](https://www.terraform.io/docs/providers/azurerm/r/dev_test_virtual_network.html) in the _Terraform Provider Documentation_