# Terraform::NSXT::LogicalPort

This resource provides a resource to configure a logical port on a logical switch in the NSX system. Like physical switches a logical switch can have one or more ports which can be connected to virtual machines or logical routers.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - ID of the logical port.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_logical_port](https://www.terraform.io/docs/providers/nsxt/r/logical_port.html) in the _Terraform Provider Documentation_