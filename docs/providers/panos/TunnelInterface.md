# Terraform::Panos::TunnelInterface

This resource allows you to add/update/delete tunnel interfaces.

## Properties

`Name` - (Required) The interface's name.  This must start with `tunnel.`.

`Vsys` - (Optional) The vsys that will use this interface (default: `vsys1`).

`Comment` - (Optional) The interface comment.

`NetflowProfile` - (Optional) The netflow profile.

`StaticIps` - (Optional) List of static IPv4 addresses to set for this data
interface.

`ManagementProfile` - (Optional) The management profile.

`Mtu` - (Optional) The MTU.


## See Also

* [panos_tunnel_interface](https://www.terraform.io/docs/providers/panos/r/tunnel_interface.html) in the _Terraform Provider Documentation_