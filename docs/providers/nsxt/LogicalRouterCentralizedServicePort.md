# Terraform::NSXT::LogicalRouterCentralizedServicePort

This resource provides a means to define a centralized service port on a logical router to connect a logical tier0 or tier1 router to a logical switch. This allows the router to be used for E-W load balancing

## Properties

`LogicalRouterId` - (Required) Identifier for logical Tier-0 or Tier-1 router on which this port is created.

`LinkedLogicalSwitchPortId` - (Required) Identifier for port on logical switch to connect to.

`IpAddress` - (Required) Logical router port subnet (ip_address / prefix length).

`UrpfMode` - (Optional) Unicast Reverse Path Forwarding mode. Accepted values are "NONE" and "STRICT" which is the default value.

`DisplayName` - (Optional) Display name, defaults to ID if not set.

`Description` - (Optional) Description of the resource.

`Tag` - (Optional) A list of scope + tag pairs to associate with this port.


## Return Values

### Fn::GetAtt

`Id` - ID of the logical router centralized service port.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_logical_router_centralized_service_port](https://www.terraform.io/docs/providers/nsxt/r/logical_router_centralized_service_port.html) in the _Terraform Provider Documentation_