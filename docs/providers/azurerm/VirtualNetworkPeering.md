# Terraform::AzureRM::VirtualNetworkPeering

Manages a virtual network peering which allows resources to access other
resources in the linked virtual network.

## Properties

`Name` - (Required) The name of the virtual network peering. Changing this
forces a new resource to be created.

`VirtualNetworkName` - (Required) The name of the virtual network. Changing
this forces a new resource to be created.

`RemoteVirtualNetworkId` - (Required) The full Azure resource ID of the
remote virtual network.  Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to
create the virtual network. Changing this forces a new resource to be
created.

`AllowVirtualNetworkAccess` - (Optional) Controls if the VMs in the remote
virtual network can access VMs in the local virtual network. Defaults to
false.

`AllowForwardedTraffic` - (Optional) Controls if forwarded traffic from  VMs
in the remote virtual network is allowed. Defaults to false.

`AllowGatewayTransit` - (Optional) Controls gatewayLinks can be used in the
remote virtual network’s link to the local virtual network.

`UseRemoteGateways` - (Optional) Controls if remote gateways can be used on
the local virtual network. If the flag is set to `true`, and
`AllowGatewayTransit` on the remote peering is also `true`, virtual network will
use gateways of remote virtual network for transit. Only one peering can
have this flag set to `true`. This flag cannot be set if virtual network
already has a gateway. Defaults to `false`.


## Return Values

### Fn::GetAtt

`Id` - The Virtual Network Peering resource ID.

## See Also

* [azurerm_virtual_network_peering](https://www.terraform.io/docs/providers/azurerm/r/virtual_network_peering.html) in the _Terraform Provider Documentation_