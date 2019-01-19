# Terraform::NSXT::StaticRoute

This resource provides a means to configure static routes in NSX to determine where IP traffic is routed.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - ID of the static route.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

`BfdEnabled` - Status of bfd for this next hop where bfd_enabled = true indicate bfd is enabled for this next hop and bfd_enabled = false indicate bfd peer is disabled or not configured for this next hop.

`BlackholeAction` - Action to be taken on matching packets for NULL routes.

## See Also

* [nsxt_static_route](https://www.terraform.io/docs/providers/nsxt/r/static_route.html) in the _Terraform Provider Documentation_