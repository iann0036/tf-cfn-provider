# Terraform::NSXT::LogicalRouterLinkPortOnTier1

This resource provides the ability to configure a logical router link port on a tier 1 logical router. This port can then be used to connect the tier 1 logical router to another logical router.

## Properties

`LogicalRouterId` - (Required) Identifier for logical tier-1 router on which this port is created.

`LinkedLogicalSwitchPortId` - (Required) Identifier for port on logical Tier-0 router to connect to.

`DisplayName` - (Optional) Display name, defaults to ID if not set.

`Description` - (Optional) Description of the resource.

`Tag` - (Optional) A list of scope + tag pairs to associate with this port.


## Return Values

### Fn::GetAtt

`Id` - ID of the logical router link port.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_logical_router_link_port_on_tier1](https://www.terraform.io/docs/providers/nsxt/r/logical_router_link_port_on_tier1.html) in the _Terraform Provider Documentation_