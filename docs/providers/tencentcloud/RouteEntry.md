# Terraform::TencentCloud::RouteEntry

Provides a resource to create a routing entry in a VPC routing table.

## Properties

`VpcId` - (Required, Forces new resource) The VPC ID.

`RouteTableId` - (Required, Forces new resource) The ID of the route table.

`CidrBlock` - (Required, Forces new resource) The RouteEntry's target network segment.

`NextType` - (Required, Forces new resource) The next hop type. Available value is `public_gateway`、`vpn_gateway`、`sslvpn_gateway`、`dc_gateway`、`peering_connection`、`nat_gateway` and `instance`. `instance` points to CVM Instance.

`NextHub` - (Required, Forces new resource) The route entry's next hub. CVM instance ID or VPC router interface ID.


## Return Values

### Fn::GetAtt

`RouteTableId` - The ID of the route table.

`CidrBlock` - The RouteEntry's target network segment.

`NextType` - The next hub type.

`NextHub` - The route entry's next hub.

## See Also

* [tencentcloud_route_entry](https://www.terraform.io/docs/providers/tencentcloud/r/route_entry.html) in the _Terraform Provider Documentation_