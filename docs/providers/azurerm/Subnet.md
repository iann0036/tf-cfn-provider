# Terraform::AzureRM::Subnet

Manages a subnet. Subnets represent network segments within the IP space defined by the virtual network.

~> **NOTE on Virtual Networks and Subnet's:** Terraform currently
provides both a standalone [Subnet resource](subnet.html), and allows for Subnets to be defined in-line within the [Virtual Network resource](virtual_network.html).
At this time you cannot use a Virtual Network with in-line Subnets in conjunction with any Subnet resources. Doing so will cause a conflict of Subnet configurations and will overwrite Subnet's.

## Properties

`Name` - (Required) The name of service to delegate to. Possible values include: `Microsoft.Batch/batchAccounts`, `Microsoft.ContainerInstance/containerGroups`, `Microsoft.HardwareSecurityModules/dedicatedHSMs`, `Microsoft.Logic/integrationServiceEnvironments`, `Microsoft.Netapp/volumes`, `Microsoft.ServiceFabricMesh/networks`, `Microsoft.Sql/managedInstances`, `Microsoft.Sql/servers` or `Microsoft.Web/serverFarms`.

`ResourceGroupName` - (Required) The name of the resource group in which to create the subnet. Changing this forces a new resource to be created.

`VirtualNetworkName` - (Required) The name of the virtual network to which to attach the subnet. Changing this forces a new resource to be created.

`AddressPrefix` - (Required) The address prefix to use for the subnet.

`NetworkSecurityGroupId` - (Optional / **Deprecated**) The ID of the Network Security Group to associate with the subnet.

`RouteTableId` - (Optional / **Deprecated**) The ID of the Route Table to associate with the subnet.

`ServiceEndpoints` - (Optional) The list of Service endpoints to associate with the subnet. Possible values include: `Microsoft.AzureActiveDirectory`, `Microsoft.AzureCosmosDB`, `Microsoft.EventHub`, `Microsoft.KeyVault`, `Microsoft.ServiceBus`, `Microsoft.Sql` and `Microsoft.Storage`.

`Delegation` - (Optional) One or more `Delegation` blocks as defined below.

`Actions` - (Optional) A list of Actions which should be delegated. Possible values include: `Microsoft.Network/virtualNetworks/subnets/action`.


## Return Values

### Fn::GetAtt

`Id` - The subnet ID.

`IpConfigurations` - The collection of IP Configurations with IPs within this subnet.

`Name` - The name of the subnet.

`ResourceGroupName` - The name of the resource group in which the subnet is created in.

`VirtualNetworkName` - The name of the virtual network in which the subnet is created in.

`AddressPrefix` - The address prefix for the subnet.

## See Also

* [azurerm_subnet](https://www.terraform.io/docs/providers/azurerm/r/subnet.html) in the _Terraform Provider Documentation_