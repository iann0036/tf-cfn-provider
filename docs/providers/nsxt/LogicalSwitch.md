# Terraform::NSXT::LogicalSwitch

This resource provides a method to create a logical switch in NSX. Virtual machines can then be connected to the appropriate logical switch for the desired topology and network connectivity.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - ID of the logical switch.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_logical_switch](https://www.terraform.io/docs/providers/nsxt/r/logical_switch.html) in the _Terraform Provider Documentation_