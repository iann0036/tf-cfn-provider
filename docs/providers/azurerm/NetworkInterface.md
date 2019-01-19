# Terraform::AzureRM::NetworkInterface

Manages a Network Interface located in a Virtual Network, usually attached to a Virtual Machine.

## Properties

`ResourceGroupName` - (Required) The name of the resource group in which to create the network interface. Changing this forces a new resource to be created.

`Location` - (Required) The location/region where the network interface is created. Changing this forces a new resource to be created.

`NetworkSecurityGroupId` - (Optional) The ID of the Network Security Group to associate with the network interface.

`InternalDnsNameLabel` - (Optional) Relative DNS name for this NIC used for internal communications between VMs in the same VNet.

`EnableIpForwarding` - (Optional) Enables IP Forwarding on the NIC. Defaults to `false`.

`EnableAcceleratedNetworking` - (Optional) Enables Azure Accelerated Networking using SR-IOV. Only certain VM instance sizes are supported. Refer to [Create a Virtual Machine with Accelerated Networking](https://docs.microsoft.com/en-us/azure/virtual-network/create-vm-accelerated-networking-cli). Defaults to `false`.

`DnsServers` - (Optional) List of DNS servers IP addresses to use for this NIC, overrides the VNet-level server list.

`IpConfiguration` - (Required) One or more `IpConfiguration` associated with this NIC as documented below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### IpConfiguration Properties

`Name` - (Required) User-defined name of the IP.

`SubnetId` - (Optional) Reference to a subnet in which this NIC has been created. Required when `PrivateIpAddressVersion` is IPv4.

`PrivateIpAddress` - (Optional) Static IP Address.

`PrivateIpAddressAllocation` - (Required) Defines how a private IP address is assigned. Options are Static or Dynamic.

`PrivateIpAddressVersion` - (Optional) The IP Version to use. Possible values are `IPv4` or `IPv6`. Defaults to `IPv4`.

`PublicIpAddressId` - (Optional) Reference to a Public IP Address to associate with this NIC.

`ApplicationGatewayBackendAddressPoolsIds` - (Optional / **Deprecated**) List of Application Gateway Backend Address Pool IDs references to which this NIC belongs.

`LoadBalancerBackendAddressPoolsIds` - (Optional / **Deprecated**) List of Load Balancer Backend Address Pool IDs references to which this NIC belongs.

`LoadBalancerInboundNatRulesIds` - (Optional / **Deprecated**) List of Load Balancer Inbound Nat Rules IDs involving this NIC.

`ApplicationSecurityGroupIds` - (Optional) List of Application Security Group IDs which should be attached to this NIC.

`Primary` - (Optional) Is this the Primary Network Interface? If set to `true` this should be the first `IpConfiguration` in the array.


## Return Values

### Fn::GetAtt

`Id` - The Virtual Network Interface ID.

`MacAddress` - The media access control (MAC) address of the network interface.

`PrivateIpAddress` - The first private IP address of the network interface.

`PrivateIpAddresses` - The private IP addresses of the network interface.

`VirtualMachineId` - Reference to a VM with which this NIC has been associated.

`AppliedDnsServers` - If the VM that uses this NIC is part of an Availability Set, then this list will have the union of all DNS servers from all NICs that are part of the Availability Set.

## See Also

* [azurerm_network_interface](https://www.terraform.io/docs/providers/azurerm/r/network_interface.html) in the _Terraform Provider Documentation_