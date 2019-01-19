# Terraform::NSXT::LogicalDhcpPort

This resource provides a resource to configure a logical port on a logical switch, and attach it to a DHCP server.

## Properties

`DisplayName` - (Optional) Display name, defaults to ID if not set.

`Description` - (Optional) Description of this resource.

`LogicalSwitchId` - (Required) Logical switch ID for the logical port.

`DhcpServerId` - (Required) Logical DHCP server ID for the logical port.

`AdminState` - (Optional) Admin state for the logical port. Accepted values - 'UP' or 'DOWN'. The default value is 'UP'.

`Tag` - (Optional) A list of scope + tag pairs to associate with this logical port.


## Return Values

### Fn::GetAtt

`Id` - ID of the logical DHCP port.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_logical_dhcp_port](https://www.terraform.io/docs/providers/nsxt/r/logical_dhcp_port.html) in the _Terraform Provider Documentation_