# Terraform::NSXT::LogicalDhcpServer

Provides a resource to configure logical DHCP server on NSX-T manager

## Properties

`DisplayName` - (Optional) The display name of this resource. Defaults to ID if not set.

`Description` - (Optional) Description of this resource.

`DhcpProfileId` - (Required) DHCP profile uuid.

`DhcpServerIp` - (Required) DHCP server IP in cidr format.

`GatewayIp` - (Required) Gateway IP.

`DomainName` - (Optional) Domain name.

`DnsNameServers` - (Optional) DNS IPs.

`DhcpOption121` - (Optional) DHCP classless static routes.
* `Network` - (Required) Destination in cidr format.
* `NextHop` - (Required) IP address of next hop.

`Network` - (Required) Destination in cidr format.
* `NextHop` - (Required) IP address of next hop.

`NextHop` - (Required) IP address of next hop.

`DhcpGenericOption` - (Optional) Generic DHCP options.
* `Code` - (Required) DHCP option code. Valid values are from 0 to 255.
* `Values` - (Required) List of DHCP option values.

`Code` - (Required) DHCP option code. Valid values are from 0 to 255.
* `Values` - (Required) List of DHCP option values.

`Values` - (Required) List of DHCP option values.

`Tag` - (Optional) A list of scope + tag pairs to associate with this logical DHCP server.


## Return Values

### Fn::GetAtt

`Id` - ID of the logical DHCP server.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

`AttachedLogicalPortId` - ID of the attached logical port.

## See Also

* [nsxt_logical_dhcp_server](https://www.terraform.io/docs/providers/nsxt/r/logical_dhcp_server.html) in the _Terraform Provider Documentation_