# Terraform::NSXT::LogicalRouterDownlinkPort

This resource provides a means to define a downlink port on a logical router to connect a logical tier1 router to a logical switch. The result of this is to provide a default gateway to virtual machines running on the logical switch.

## Properties

`LogicalRouterId` - (Required) Identifier for logical Tier-1 router on which this port is created.

`LinkedLogicalSwitchPortId` - (Required) Identifier for port on logical switch to connect to.

`IpAddress` - (Required) Logical router port subnet (ip_address / prefix length).

`UrpfMode` - (Optional) Unicast Reverse Path Forwarding mode. Accepted values are "NONE" and "STRICT" which is the default value.

`DisplayName` - (Optional) Display name, defaults to ID if not set.

`Description` - (Optional) Description of the resource.

`Tag` - (Optional) A list of scope + tag pairs to associate with this port.

`ServiceBinding` - (Optional) A list of services for this port. Currently only "LogicalService" is supported as a target_type, and a DHCP relay service ID as target_id.


## Return Values

### Fn::GetAtt

`Id` - ID of the logical router downlink port.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

`MacAddress` - The MAC address assigned to this port.

## See Also

* [nsxt_logical_router_downlink_port](https://www.terraform.io/docs/providers/nsxt/r/logical_router_downlink_port.html) in the _Terraform Provider Documentation_