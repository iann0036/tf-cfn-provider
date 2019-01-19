# Terraform::NSXT::LogicalPort

This resource provides a resource to configure a logical port on a logical switch in the NSX system. Like physical switches a logical switch can have one or more ports which can be connected to virtual machines or logical routers.

## Properties

`DisplayName` - (Optional) Display name, defaults to ID if not set.

`Description` - (Optional) Description of this resource.

`LogicalSwitchId` - (Required) Logical switch ID for the logical port.

`AdminState` - (Optional) Admin state for the logical port. Accepted values - 'UP' or 'DOWN'. The default value is 'UP'.

`SwitchingProfileId` - (Optional) List of IDs of switching profiles (of various types) to be associated with this switch. Default switching profiles will be used if not specified.

`Tag` - (Optional) A list of scope + tag pairs to associate with this logical port.


## Return Values

### Fn::GetAtt

`Id` - ID of the logical port.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_logical_port](https://www.terraform.io/docs/providers/nsxt/r/logical_port.html) in the _Terraform Provider Documentation_