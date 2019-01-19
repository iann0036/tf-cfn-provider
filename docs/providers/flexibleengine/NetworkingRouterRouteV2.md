# Terraform::FlexibleEngine::NetworkingRouterRouteV2

Creates a routing entry on a FlexibleEngine V2 router.

## Properties

`Region` - (Optional) The region in which to obtain the V2 networking client. A networking client is needed to configure a routing entry on a router. If omitted, the `Region` argument of the provider is used. Changing this creates a new routing entry.

`RouterId` - (Required) ID of the router this routing entry belongs to. Changing this creates a new routing entry.

`DestinationCidr` - (Required) CIDR block to match on the packet’s destination IP. Changing this creates a new routing entry.

`NextHop` - (Required) IP address of the next hop gateway.  Changing this creates a new routing entry.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`RouterId` - See Properties above.

`DestinationCidr` - See Properties above.

`NextHop` - See Properties above.

## See Also

* [flexibleengine_networking_router_route_v2](https://www.terraform.io/docs/providers/flexibleengine/r/networking_router_route_v2.html) in the _Terraform Provider Documentation_