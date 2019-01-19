# Terraform::AzureStack::VirtualNetwork

Creates a new virtual network including any configured subnets. Each subnet can
optionally be configured with a security group to be associated with the subnet.

~> **NOTE on Virtual Networks and Subnet's:** Terraform currently
provides both a standalone [Subnet resource](subnet.html), and allows for Subnets to be defined in-line within the [Virtual Network resource](virtual_network.html).
At this time you cannot use a Virtual Network with in-line Subnets in conjunction with any Subnet resources. Doing so will cause a conflict of Subnet configurations and will overwrite Subnets.

## Properties

`ResourceGroupName` - (Required) The name of the resource group in which to create the virtual network.

`AddressSpace` - (Required) The address space that is used the virtual network. You can supply more than one address space. Changing this forces a new resource to be created.

`Location` - (Required) The location/region where the virtual network is created. Changing this forces a new resource to be created.

`DnsServers` - (Optional) List of IP addresses of DNS servers.

`Subnet` - (Optional) Can be specified multiple times to define multiple subnets. Each `Subnet` block supports fields documented below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### Subnet Properties

`Name` - (Required) The name of the subnet.

`AddressPrefix` - (Required) The address prefix to use for the subnet.

`SecurityGroup` - (Optional) The Network Security Group to associate with the subnet. (Referenced by `id`, ie. `Terraform::AzureStack::NetworkSecurityGroup.test.id`).


## Return Values

### Fn::GetAtt

`Id` - The virtual NetworkConfiguration ID.

`Name` - The name of the virtual network.

`ResourceGroupName` - The name of the resource group in which to create the virtual network.

`Location` - The location/region where the virtual network is created.

`AddressSpace` - The address space that is used the virtual network.

## See Also

* [azurestack_virtual_network](https://www.terraform.io/docs/providers/azurestack/r/virtual_network.html) in the _Terraform Provider Documentation_