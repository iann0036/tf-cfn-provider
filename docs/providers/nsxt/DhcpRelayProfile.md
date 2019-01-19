# Terraform::NSXT::DhcpRelayProfile

This resource can be used to configure a NSX DHCP relay profile on the NSX manager.
A DHCP relay profile is a type of template that can be used to define a remote DHCP server
where DHCP packets can be relayed for DHCP requests of machines attached to NSX logical topologies.
The DHCP relay profile can be used in a DHCP relay service and later consumed by a router
downlink port.
Currently the DHCP relay is not supported for logical routers link ports on Tier0 or Tier1.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - ID of the DHCP relay profile.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_dhcp_relay_profile](https://www.terraform.io/docs/providers/nsxt/r/dhcp_relay_profile.html) in the _Terraform Provider Documentation_