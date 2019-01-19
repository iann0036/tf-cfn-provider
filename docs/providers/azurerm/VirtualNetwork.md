# Terraform::AzureRM::VirtualNetwork

Manages a virtual network including any configured subnets. Each subnet can
optionally be configured with a security group to be associated with the subnet.

~> **NOTE on Virtual Networks and Subnet's:** Terraform currently
provides both a standalone [Subnet resource](subnet.html), and allows for Subnets to be defined in-line within the [Virtual Network resource](virtual_network.html).
At this time you cannot use a Virtual Network with in-line Subnets in conjunction with any Subnet resources. Doing so will cause a conflict of Subnet configurations and will overwrite Subnet's.

## Properties

`ResourceGroupName` - (Required) The name of the resource group in which to create the virtual network.

`AddressSpace` - (Required) The address space that is used the virtual network. You can supply more than one address space. Changing this forces a new resource to be created.

`Location` - (Required) The location/region where the virtual network is created. Changing this forces a new resource to be created.

`DdosProtectionPlan` - (Optional) A `DdosProtectionPlan` block as documented below.

`DnsServers` - (Optional) List of IP addresses of DNS servers.

`Subnet` - (Optional) Can be specified multiple times to define multiple subnets. Each `Subnet` block supports fields documented below.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### DdosProtectionPlan Properties

`Id` - (Required) The Resource ID of DDoS Protection Plan.

`Enable` - (Required) Enable/disable DDoS Protection Plan on Virtual Network. Defaults to `false`.

### Subnet Properties

`Name` - (Required) The name of the subnet.

`AddressPrefix` - (Required) The address prefix to use for the subnet.

`SecurityGroup` - (Optional) The Network Security Group to associate with the subnet. (Referenced by `Id`, ie. `Terraform::AzureRM::NetworkSecurityGroup.test.id`).


## Return Values

### Fn::GetAtt

`Id` - The ID of this subnet.

`Name` - The name of the virtual network.

`ResourceGroupName` - The name of the resource group in which to create the virtual network.

`Location` - The location/region where the virtual network is created.

`AddressSpace` - The address space that is used the virtual network.

`Subnet` - One or more `Subnet` blocks as defined below.

## See Also

* [azurerm_virtual_network](https://www.terraform.io/docs/providers/azurerm/r/virtual_network.html) in the _Terraform Provider Documentation_