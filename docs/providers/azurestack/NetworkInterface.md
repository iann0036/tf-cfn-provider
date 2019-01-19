# Terraform::AzureStack::NetworkInterface

Manages a Network Interface located in a Virtual Network, usually attached to a Virtual Machine.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The Virtual Network Interface ID.

`MacAddress` - The media access control (MAC) address of the network interface.

`PrivateIpAddress` - The private ip address of the network interface.

`VirtualMachineId` - Reference to a VM with which this NIC has been associated.

`AppliedDnsServers` - If the VM that uses this NIC is part of an Availability Set, then this list will have the union of all DNS servers from all NICs that are part of the Availability Set.

`InternalFqdn` - Fully qualified DNS name supporting internal communications between VMs in the same VNet.

## See Also

* [azurestack_network_interface](https://www.terraform.io/docs/providers/azurestack/r/network_interface.html) in the _Terraform Provider Documentation_