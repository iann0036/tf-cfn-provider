# Terraform::Google::ComputeRouterInterface

Manages a Cloud Router interface. For more information see
[the official documentation](https://cloud.google.com/compute/docs/cloudrouter)
and
[API](https://cloud.google.com/compute/docs/reference/latest/routers).

## Properties

`Name` - (Required) A unique name for the interface, required by GCE. Changing
this forces a new interface to be created.

`Router` - (Required) The name of the router this interface will be attached to.
Changing this forces a new interface to be created.

`VpnTunnel` - (Required) The name or resource link to the VPN tunnel this
interface will be linked to. Changing this forces a new interface to be created.

`IpRange` - (Optional) IP address and range of the interface. The IP range must be
in the RFC3927 link-local IP space. Changing this forces a new interface to be created.

`Project` - (Optional) The ID of the project in which this interface's router belongs. If it
is not provided, the provider project is used. Changing this forces a new interface to be created.

`Region` - (Optional) The region this interface's router sits in. If not specified,
the project region will be used. Changing this forces a new interface to be
created.


## See Also

* [google_compute_router_interface](https://www.terraform.io/docs/providers/google/r/compute_router_interface.html) in the _Terraform Provider Documentation_