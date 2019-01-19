# Terraform::NSXT::LbService

Provides a resource to configure lb service on NSX-T manager.
Note that lb service needs to be attached to Tier-1 router that satisfies
following preconditions:
* It needs to reside on edge cluster
* It needs to be condigured with either uplink port or centralized service port

In order to enforce correct order of create/delete, it is recommended to add
depends_on clause to lb service.

## Properties

`Description` - (Optional) Description of this resource.

`DisplayName` - (Optional) The display name of this resource. Defaults to ID if not set.

`Tag` - (Optional) A list of scope + tag pairs to associate with this lb service.

`LogicalRouterId` - (Required) Tier1 logical router this service is attached to. Note that this router needs to have edge cluster configured, and have an uplink port or CSP (centralized service port).

`Enabled` - (Optional) whether the load balancer service is enabled.

`ErrorLogLevel` - (Optional) Load balancer engine writes information about encountered issues of different severity levels to the error log. This setting is used to define the severity level of the error log.

`Size` - (Required) Size of load balancer service. Accepted values are SMALL/MEDIUM/LARGE.

`VirtualServerIds` - (Optional) Virtual servers associated with this Load Balancer.


## Return Values

### Fn::GetAtt

`Id` - ID of the lb_service.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_lb_service](https://www.terraform.io/docs/providers/nsxt/r/lb_service.html) in the _Terraform Provider Documentation_