# Terraform::NSXT::VlanLogicalSwitch

This resource provides a method to create vlan logical switch in NSX. Virtual machines can then be connected to the appropriate logical switch for the desired topology and network connectivity.

## Properties

`TransportZoneId` - (Required) Transport Zone ID for the logical switch.

`AdminState` - (Optional) Admin state for the logical switch. Accepted values - 'UP' or 'DOWN'. The default value is 'UP'.

`Vlan` - (Required) Vlan for the logical switch.

`SwitchingProfileId` - (Optional) List of IDs of switching profiles (of various types) to be associated with this switch. Default switching profiles will be used if not specified.

`DisplayName` - (Optional) Display name, defaults to ID if not set.

`Description` - (Optional) Description of the resource.

`IpPoolId` - (Optional) Ip Pool ID to be associated with the logical switch.

`MacPoolId` - (Optional) Mac Pool ID to be associated with the logical switch.

`AddressBinding` - (Optional) List of Address Bindings for the logical switch. This setting allows to provide bindings between IP address, mac Address and vlan.

`Tag` - (Optional) A list of scope + tag pairs to associate with this logical switch.


## Return Values

### Fn::GetAtt

`Id` - ID of the logical switch.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_vlan_logical_switch](https://www.terraform.io/docs/providers/nsxt/r/vlan_logical_switch.html) in the _Terraform Provider Documentation_