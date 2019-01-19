# Terraform::NSXT::LogicalDhcpServer

Provides a resource to configure logical DHCP server on NSX-T manager

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - ID of the logical DHCP server.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

`AttachedLogicalPortId` - ID of the attached logical port.

## See Also

* [nsxt_logical_dhcp_server](https://www.terraform.io/docs/providers/nsxt/r/logical_dhcp_server.html) in the _Terraform Provider Documentation_