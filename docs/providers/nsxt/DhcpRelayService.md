# Terraform::NSXT::DhcpRelayService

This resource provides a way to configure the DHCP relay service on the NSX manager.
The DHCP relay service uses a DHCP relay profile and later consumed by a router
downlink port to provide DHCP addresses to virtual machines connected to a logical switch.
Currently the DHCP relay is not supported for logical routers link ports on Tier0 or Tier1.

## Properties

`Description` - (Optional) Description of this resource.

`DisplayName` - (Optional) The display name of this resource. Defaults to ID if not set.

`Tag` - (Optional) A list of scope + tag pairs to associate with this dhcp_relay_service.

`DhcpRelayProfileId` - (Required) DHCP relay profile referenced by the DHCP relay service.


## Return Values

### Fn::GetAtt

`Id` - ID of the DHCP relay service.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_dhcp_relay_service](https://www.terraform.io/docs/providers/nsxt/r/dhcp_relay_service.html) in the _Terraform Provider Documentation_