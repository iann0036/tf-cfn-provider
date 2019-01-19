# Terraform::AzureRM::VirtualNetwork

Manages a virtual network including any configured subnets. Each subnet can
optionally be configured with a security group to be associated with the subnet.

~> **NOTE on Virtual Networks and Subnet's:** Terraform currently
provides both a standalone [Subnet resource](subnet.html), and allows for Subnets to be defined in-line within the [Virtual Network resource](virtual_network.html).
At this time you cannot use a Virtual Network with in-line Subnets in conjunction with any Subnet resources. Doing so will cause a conflict of Subnet configurations and will overwrite Subnet's.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of this subnet.

`Name` - The name of the virtual network.

`ResourceGroupName` - The name of the resource group in which to create the virtual network.

`Location` - The location/region where the virtual network is created.

`AddressSpace` - The address space that is used the virtual network.

`Subnet` - One or more `subnet` blocks as defined below.

## See Also

* [azurerm_virtual_network](https://www.terraform.io/docs/providers/azurerm/r/virtual_network.html) in the _Terraform Provider Documentation_