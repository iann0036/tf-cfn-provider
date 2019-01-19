# Terraform::NSXT::DhcpServerIpPool

Provides a resource to configure IP Pool for logical DHCP server on NSX-T manager

## Properties

`DisplayName` - (Optional) The display name of this resource. Defaults to ID if not set.

`Description` - (Optional) Description of this resource.

`LogicalDhcpServerId` - (Required) DHCP server uuid. Changing this would force new pool to be created.

`GatewayIp` - (Optional) Gateway IP.

`IpRange` - (Required) IP Ranges to be used within this pool. * `Start` - (Required) IP address that indicates range start. * `End` - (Required) IP address that indicates range end.

`Start` - (Required) IP address that indicates range start. * `End` - (Required) IP address that indicates range end.

`End` - (Required) IP address that indicates range end.

`LeaseTime` - (Optional) Lease time in seconds. Default is 86400.

`ErrorThreshold` - (Optional) Error threshold in percent. Valid values are from 80 to 100, default is 100.

`WarningThreshold` - (Optional) Warning threshold in percent. Valid values are from 50 to 80, default is 80.

`DhcpOption121` - (Optional) DHCP classless static routes. If specified, overrides DHCP server settings. * `Network` - (Required) Destination in cidr format. * `NextHop` - (Required) IP address of next hop.

`Network` - (Required) Destination in cidr format. * `NextHop` - (Required) IP address of next hop.

`NextHop` - (Required) IP address of next hop.

`DhcpGenericOption` - (Optional) Generic DHCP options. If specified, overrides DHCP server settings. * `Code` - (Required) DHCP option code. Valid values are from 0 to 255. * `Values` - (Required) List of DHCP option values.

`Code` - (Required) DHCP option code. Valid values are from 0 to 255. * `Values` - (Required) List of DHCP option values.

`Values` - (Required) List of DHCP option values.

`Tag` - (Optional) A list of scope + tag pairs to associate with this logical DHCP server.


## Return Values

### Fn::GetAtt

`Id` - ID of the DHCP server IP pool.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_dhcp_server_ip_pool](https://www.terraform.io/docs/providers/nsxt/r/dhcp_server_ip_pool.html) in the _Terraform Provider Documentation_