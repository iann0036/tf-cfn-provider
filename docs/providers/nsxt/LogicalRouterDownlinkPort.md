# Terraform::NSXT::LogicalRouterDownlinkPort

This resource provides a means to define a downlink port on a logical router to connect a logical tier1 router to a logical switch. The result of this is to provide a default gateway to virtual machines running on the logical switch.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - ID of the logical router downlink port.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

`MacAddress` - The MAC address assigned to this port.

## See Also

* [nsxt_logical_router_downlink_port](https://www.terraform.io/docs/providers/nsxt/r/logical_router_downlink_port.html) in the _Terraform Provider Documentation_