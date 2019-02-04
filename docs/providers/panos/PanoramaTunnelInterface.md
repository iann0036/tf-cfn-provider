# Terraform::Panos::PanoramaTunnelInterface

This resource allows you to add/update/delete Panorama tunnel interfaces
for templates.

## Properties

`Name` - (Required) The interface's name.  This must start with `tunnel.`.

`Template` - (Required) The template name.

`Vsys` - (Optional) The vsys that will use this interface (default: `vsys1`).

`Comment` - (Optional) The interface comment.

`NetflowProfile` - (Optional) The netflow profile.

`StaticIps` - (Optional) List of static IPv4 addresses to set for this data
interface.

`ManagementProfile` - (Optional) The management profile.

`Mtu` - (Optional) The MTU.


## See Also

* [panos_panorama_tunnel_interface](https://www.terraform.io/docs/providers/panos/r/panorama_tunnel_interface.html) in the _Terraform Provider Documentation_