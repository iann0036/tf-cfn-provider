# Terraform::Alicloud::RouteEntry

Provides a route entry resource. A route entry represents a route item of one VPC route table.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`RouterId` - The ID of the virtual router attached to Vpc.

`RouteTableId` - The ID of the route table.

`DestinationCidrblock` - The RouteEntry's target network segment.

`NexthopType` - The next hop type.

`NexthopId` - The route entry's next hop.

## See Also

* [alicloud_route_entry](https://www.terraform.io/docs/providers/alicloud/r/route_entry.html) in the _Terraform Provider Documentation_