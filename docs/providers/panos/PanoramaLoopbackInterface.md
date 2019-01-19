# Terraform::Panos::PanoramaLoopbackInterface

This resource allows you to add/update/delete Panorama loopback interfaces
for templates.

## Properties

`Name` - (Required) The interface's name.  This must start with `loopback.`.

`Template` - (Required) The template name.

`Vsys` - (Optional) The vsys that will use this interface (default: `vsys1`).

`Comment` - (Optional) The interface comment.

`NetflowProfile` - (Optional) The netflow profile.

`StaticIps` - (Optional) List of static IPv4 addresses to set for this data interface.

`ManagementProfile` - (Optional) The management profile.

`Mtu` - (Optional) The MTU.

`AdjustTcpMss` - (Optional, bool) Adjust TCP MSS (default: false).

`Ipv4MssAdjust` - (Optional, PAN-OS 8.0+) The IPv4 MSS adjust value.

`Ipv6MssAdjust` - (Optional, PAN-OS 8.0+) The IPv6 MSS adjust value.


## See Also

* [panos_panorama_loopback_interface](https://www.terraform.io/docs/providers/panos/r/panorama_loopback_interface.html) in the _Terraform Provider Documentation_