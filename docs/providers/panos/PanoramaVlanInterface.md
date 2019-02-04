# Terraform::Panos::PanoramaVlanInterface

This resource allows you to add/update/delete Panorama VLAN interfaces
for templates.

## Properties

`Name` - (Required) The interface's name.  Must start with `vlan.`.

`Template` - (Required) The template name.

`Vsys` - (Optional) The vsys that will use this interface (default: `vsys1`).

`Comment` - (Optional) The interface comment.

`NetflowProfile` - (Optional) The netflow profile.

`StaticIps` - (Optional) List of static IPv4 addresses to set for this data
interface.

`EnableDhcp` - (Optional) Set to `true` to enable DHCP on this interface.

`CreateDhcpDefaultRoute` - (Optional) Set to `true` to create a DHCP
default route.

`DhcpDefaultRouteMetric` - (Optional) The metric for the DHCP default
route.

`ManagementProfile` - (Optional) The management profile.

`Mtu` - (Optional) The MTU.

`AdjustTcpMss` - (Optional) Adjust TCP MSS (default: false).

`Ipv4MssAdjust` - (Optional, PAN-OS 8.0+) The IPv4 MSS adjust value.

`Ipv6MssAdjust` - (Optional, PAN-OS 8.0+) The IPv6 MSS adjust value.


## See Also

* [panos_panorama_vlan_interface](https://www.terraform.io/docs/providers/panos/r/panorama_vlan_interface.html) in the _Terraform Provider Documentation_