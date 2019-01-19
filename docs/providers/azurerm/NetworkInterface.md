# Terraform::AzureRM::NetworkInterface

Manages a Network Interface located in a Virtual Network, usually attached to a Virtual Machine.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The Virtual Network Interface ID.

`MacAddress` - The media access control (MAC) address of the network interface.

`PrivateIpAddress` - The first private IP address of the network interface.

`PrivateIpAddresses` - The private IP addresses of the network interface.

`VirtualMachineId` - Reference to a VM with which this NIC has been associated.

`AppliedDnsServers` - If the VM that uses this NIC is part of an Availability Set, then this list will have the union of all DNS servers from all NICs that are part of the Availability Set.

## See Also

* [azurerm_network_interface](https://www.terraform.io/docs/providers/azurerm/r/network_interface.html) in the _Terraform Provider Documentation_