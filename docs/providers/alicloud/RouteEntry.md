# Terraform::Alicloud::RouteEntry

Provides a route entry resource. A route entry represents a route item of one VPC route table.

## Properties

`RouterId` - (Deprecated) This argument has beeb deprecated. Please use other arguments to launch a custom route entry.

`RouteTableId` - (Required, Forces new resource) The ID of the route table.

`DestinationCidrblock` - (Required, Forces new resource) The RouteEntry's target network segment.

`NexthopType` - (Required, Forces new resource) The next hop type. Available values:
- `Instance` (Default): Route the traffic destined for the destination CIDR block to an ECS instance in the VPC.
- `RouterInterface`: Route the traffic destined for the destination CIDR block to a router interface.
- `VpnGateway`: Route the traffic destined for the destination CIDR block to a VPN Gateway.
- `HaVip`: Route the traffic destined for the destination CIDR block to an HAVIP.
- `NetworkInterface`: Route the traffic destined for the destination CIDR block to an NetworkInterface.
- `NatGateway`: Route the traffic destined for the destination CIDR block to an Nat Gateway.

`NexthopId` - (Required, Forces new resource) The route entry's next hop. ECS instance ID or VPC router interface ID.


## Return Values

### Fn::GetAtt

`RouterId` - The ID of the virtual router attached to Vpc.

`RouteTableId` - The ID of the route table.

`DestinationCidrblock` - The RouteEntry's target network segment.

`NexthopType` - The next hop type.

`NexthopId` - The route entry's next hop.

## See Also

* [alicloud_route_entry](https://www.terraform.io/docs/providers/alicloud/r/route_entry.html) in the _Terraform Provider Documentation_