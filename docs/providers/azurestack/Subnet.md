# Terraform::AzureStack::Subnet

Manages a subnet. Subnets represent network segments within the IP space defined by the virtual network.

~> **NOTE on Virtual Networks and Subnet's:** Terraform currently
provides both a standalone [Subnet resource](subnet.html), and allows for Subnets to be defined in-line within the [Virtual Network resource](virtual_network.html).
At this time you cannot use a Virtual Network with in-line Subnets in conjunction with any Subnet resources. Doing so will cause a conflict of Subnet configurations and will overwrite Subnet's.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The subnet ID.

`IpConfigurations` - The collection of IP Configurations with IPs within this subnet.

`Name` - The name of the subnet.

`ResourceGroupName` - The name of the resource group in which the subnet is created in.

`VirtualNetworkName` - The name of the virtual network in which the subnet is created in.

`AddressPrefix` - The address prefix for the subnet.

## See Also

* [azurestack_subnet](https://www.terraform.io/docs/providers/azurestack/r/subnet.html) in the _Terraform Provider Documentation_