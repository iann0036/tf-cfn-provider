# Terraform::AzureStack::VirtualNetworkGateway

Manages a Virtual Network Gateway to establish secure, cross-premises connectivity.

## Properties

`Name` - (Required) The name of the connection. Changing the name forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the connection Changing the name forces a new resource to be created.

`Location` - (Required) The location/region where the connection is located. Changing this forces a new resource to be created.

`Type` - (Required) The type of the Virtual Network Gateway. Valid options is `Vpn`.

`VpnType` - (Optional) The routing type of the Virtual Network Gateway. Only valid option is `RouteBased`.

`EnableBgp` - (Optional) If `true`, BGP (Border Gateway Protocol) is enabled for this connection. Defaults to `false`.

`Sku` - (Required) Configuration of the size and capacity of the virtual network gateway. Valid options are `Basic`, `Standard` and `HighPerformance`.

`IpConfiguration` - (Required) One or two ip_configuration blocks documented below. An active-standby gateway requires exactly one ip_configuration block whereas an active-active gateway requires exactly two ip_configuration blocks.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### IpConfiguration Properties

`Name` - (Optional) A user-defined name of the IP configuration. Defaults to vnetGatewayConfig.

`PrivateIpAddressAllocation` - (Optional) Defines how the private IP address of the gateways virtual interface is assigned. Valid options are Static or Dynamic. Defaults to Dynamic.

`SubnetId` - (Required) The ID of the gateway subnet of a virtual network in which the virtual network gateway will be created. It is mandatory that the associated subnet is named `GatewaySubnet`. Therefore, each virtual network can contain at most a single Virtual Network Gateway.

`PublicIpAddressId` - (Optional) The ID of the public ip address to associate with the Virtual Network Gateway.

`Asn` - (Optional) The Autonomous System Number (ASN) to use as part of the BGP.

`PeeringAddress` - (Optional) The BGP peer IP address of the virtual network gateway. This address is needed to configure the created gateway as a BGP Peer on the on-premises VPN devices. The IP address must be part of the subnet of the Virtual Network Gateway. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Virtual Network Gateway.

## See Also

* [azurestack_virtual_network_gateway](https://www.terraform.io/docs/providers/azurestack/r/virtual_network_gateway.html) in the _Terraform Provider Documentation_