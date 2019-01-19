# Terraform::NSXT::StaticRoute

This resource provides a means to configure static routes in NSX to determine where IP traffic is routed.

## Properties

`Description` - (Optional) Description of this resource.

`DisplayName` - (Optional) The display name of this resource. Defaults to ID if not set.

`Tag` - (Optional) A list of scope + tag pairs to associate with this static route.

`LogicalRouterId` - (Required) Logical router id.

`Network` - (Required) CIDR.

`NextHop` - (Required) List of Next Hops, each with those arguments: * `AdministrativeDistance` - (Optional) Administrative Distance for the next hop IP. * `IpAddress` - (Optional) Next Hop IP. * `LogicalRouterPortId` - (Optional) Reference of logical router port to be used for next hop.

`AdministrativeDistance` - (Optional) Administrative Distance for the next hop IP. * `IpAddress` - (Optional) Next Hop IP. * `LogicalRouterPortId` - (Optional) Reference of logical router port to be used for next hop.

`IpAddress` - (Optional) Next Hop IP. * `LogicalRouterPortId` - (Optional) Reference of logical router port to be used for next hop.

`LogicalRouterPortId` - (Optional) Reference of logical router port to be used for next hop.


## Return Values

### Fn::GetAtt

`Id` - ID of the static route.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

`BfdEnabled` - Status of bfd for this next hop where bfd_enabled = true indicate bfd is enabled for this next hop and bfd_enabled = false indicate bfd peer is disabled or not configured for this next hop.

`BlackholeAction` - Action to be taken on matching packets for NULL routes.

## See Also

* [nsxt_static_route](https://www.terraform.io/docs/providers/nsxt/r/static_route.html) in the _Terraform Provider Documentation_