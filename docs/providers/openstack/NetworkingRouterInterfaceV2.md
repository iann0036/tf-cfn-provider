# Terraform::OpenStack::NetworkingRouterInterfaceV2

Manages a V2 router interface resource within OpenStack.

## Properties

`Region` - (Optional) The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
`Region` argument of the provider is used. Changing this creates a new
router interface.

`RouterId` - (Required) ID of the router this interface belongs to. Changing
this creates a new router interface.

`SubnetId` - ID of the subnet this interface connects to. Changing
this creates a new router interface.

`PortId` - ID of the port this interface connects to. Changing
this creates a new router interface.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`RouterId` - See Properties above.

`SubnetId` - See Properties above.

`PortId` - See Properties above.

## See Also

* [openstack_networking_router_interface_v2](https://www.terraform.io/docs/providers/openstack/r/networking_router_interface_v2.html) in the _Terraform Provider Documentation_