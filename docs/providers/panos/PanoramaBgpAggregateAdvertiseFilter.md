# Terraform::Panos::PanoramaBgpAggregateAdvertiseFilter

This resource allows you to add/update/delete a Panorama route advertise filter for a
BGP address aggregation rule.

## Properties

`Template` - The template name.

`TemplateStack` - The template stack name.

`VirtualRouter` - (Required) The virtual router to add this filter to.

`BgpAggregate` - (Required) The BGP address aggregation rule.

`Name` - (Required) The name.

`Enable` - (Optional, bool) Enable or not (default: `true`).

`AsPathRegex` - (Optional) AS path to match.

`CommunityRegex` - (Optional) Community to match.

`ExtendedCommunityRegex` - (Optional) Extended community to match.

`Med` - (Optional) Match MED.

`RouteTable` - (Optional, PAN-OS 8.0+) Route table to match rule.  Valid
values are `unicast`, `multicast`, or `both`.

`AddressPrefix` - (Optional, repeatable) Matching address prefix definition
(see below).

`NextHops` - (Optional) List of next hop attributes.

`FromPeers` - (Optional) List of peers that advertised the route entry.

### AddressPrefix Properties

`Prefix` - (Required) Address prefix.

`Exact` - (Optional, bool) Match exact prefix length.


## See Also

* [panos_panorama_bgp_aggregate_advertise_filter](https://www.terraform.io/docs/providers/panos/r/panorama_bgp_aggregate_advertise_filter.html) in the _Terraform Provider Documentation_