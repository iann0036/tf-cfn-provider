# Terraform::TencentCloud::RouteEntry

Provides a resource to create a routing entry in a VPC routing table.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`RouteTableId` - The ID of the route table.

`CidrBlock` - The RouteEntry's target network segment.

`NextType` - The next hub type.

`NextHub` - The route entry's next hub.

## See Also

* [tencentcloud_route_entry](https://www.terraform.io/docs/providers/tencentcloud/r/route_entry.html) in the _Terraform Provider Documentation_