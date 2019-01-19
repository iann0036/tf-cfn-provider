# Terraform::NSXT::LbService

Provides a resource to configure lb service on NSX-T manager.
Note that lb service needs to be attached to Tier-1 router that satisfies
following preconditions:
* It needs to reside on edge cluster
* It needs to be condigured with either uplink port or centralized service port

In order to enforce correct order of create/delete, it is recommended to add
depends_on clause to lb service.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - ID of the lb_service.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_lb_service](https://www.terraform.io/docs/providers/nsxt/r/lb_service.html) in the _Terraform Provider Documentation_