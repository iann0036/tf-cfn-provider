# Terraform::NSXT::DhcpRelayService

This resource provides a way to configure the DHCP relay service on the NSX manager.
The DHCP relay service uses a DHCP relay profile and later consumed by a router
downlink port to provide DHCP addresses to virtual machines connected to a logical switch.
Currently the DHCP relay is not supported for logical routers link ports on Tier0 or Tier1.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - ID of the DHCP relay service.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_dhcp_relay_service](https://www.terraform.io/docs/providers/nsxt/r/dhcp_relay_service.html) in the _Terraform Provider Documentation_