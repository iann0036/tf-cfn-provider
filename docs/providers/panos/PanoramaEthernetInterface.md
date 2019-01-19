# Terraform::Panos::PanoramaEthernetInterface

This resource allows you to add/update/delete Panorama ethernet interfaces
for templates.

## Properties

`Name` - (Required) The ethernet interface's name.  This should be something like `ethernet1/X`.

`Template` - (Required) The template name.

`Vsys` - (Optional) The vsys that will use this interface (default: `vsys1`).  This should be something like `vsys1` or `vsys3`.

`Mode` - (Required) The interface mode.  This can be any of the following values: `layer3`, `layer2`, `virtual-wire`, `tap`, `ha`, `decrypt-mirror`, or `aggregate-group`.

`StaticIps` - (Optional) List of static IPv4 addresses to set for this data interface.

`EnableDhcp` - (Optional) Set to `true` to enable DHCP on this interface.

`CreateDhcpDefaultRoute` - (Optional) Set to `true` to create a DHCP default route.

`DhcpDefaultRouteMetric` - (Optional) The metric for the DHCP default route.

`Ipv6Enabled` - (Optional) Set to `true` to enable IPv6.

`ManagementProfile` - (Optional) The management profile.

`Mtu` - (Optional) The MTU.

`AdjustTcpMss` - (Optional) Adjust TCP MSS (default: false).

`NetflowProfile` - (Optional) The netflow profile.

`LldpEnabled` - (Optional) Enable LLDP (default: false).

`LldpProfile` - (Optional) LLDP profile.

`LinkSpeed` - (Optional) Link speed.  This can be any of the following: `10`, `100`, `1000`, or `auto`.

`LinkDuplex` - (Optional) Link duplex setting.  This can be `full`, `half`, or `auto`.

`LinkState` - (Optional) The link state.  This can be `up`, `down`, or `auto`.

`AggregateGroup` - (Optional) The aggregate group (applicable for physical firewalls only).

`Comment` - (Optional) The interface comment.

`Ipv4MssAdjust` - (Optional, PAN-OS 8.0+) The IPv4 MSS adjust value.

`Ipv6MssAdjust` - (Optional, PAN-OS 8.0+) The IPv6 MSS adjust value.


## See Also

* [panos_panorama_ethernet_interface](https://www.terraform.io/docs/providers/panos/r/panorama_ethernet_interface.html) in the _Terraform Provider Documentation_