# Terraform::Panos::PanoramaStaticRouteIpv4

This resource allows you to add/update/delete Panorama IPv4 static routes on a
virtual router for either a template or a template stack.

## Properties

`Template` - The template name.

`TemplateStack` - The template stack name.

`Name` - (Required) The static route's name.

`VirtualRouter` - (Required) The virtual router to add the static
route to.

`Destination` - (Required) Destination IP address / prefix.

`Interface` - (Optional) Interface to use.

`Type` - (Optional) The next hop type.  Valid values are `ip-address` (the
default), `discard`, `next-vr`, or an empty string for `None`.

`NextHop` - (Optional) The value for the `Type` setting.

`AdminDistance` - (Optional) The admin distance.

`Metric` - (Optional, int) Metric value / path cost (default: `10`).

`RouteTable` - (Optional) Target routing table to install the route.  Valid
values are `unicast` (the default), `no install`, `multicast`, or `both`.

`BfdProfile` - (Optional, PAN-OS 7.1+) BFD configuration.


## See Also

* [panos_panorama_static_route_ipv4](https://www.terraform.io/docs/providers/panos/r/panorama_static_route_ipv4.html) in the _Terraform Provider Documentation_