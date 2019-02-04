# Terraform::Panos::PanoramaBgpConditionalAdvNonExistFilter

This resource allows you to add/update/delete a Panorama non-exist filter for a
BGP conditional advertisement.

~> **Note:** A BGP conditional advertisement is valid only if there is at least
one non-exist filter and one advertise filter attached.  This filter must be paired
with the other in order for the configuration to be valid.

## Properties

`Template` - The template name.

`TemplateStack` - The template stack name.

`VirtualRouter` - (Required) The virtual router to add this filter to.

`BgpConditionalAdv` - (Required) The BGP conditional advertisement to add
this filter to.

`Name` - (Required) The name.

`Enable` - (Optional, bool) Enable or not (default: `true`).

`AsPathRegex` - (Optional) AS path to match.

`CommunityRegex` - (Optional) Community to match.

`ExtendedCommunityRegex` - (Optional) Extended community to match.

`Med` - (Optional) Match MED.

`RouteTable` - (Optional, PAN-OS 8.0+) Route table to match rule.  Valid
values are `unicast`, `multicast`, or `both`.  As of PAN-OS 8.1, there doesn't
seem to be a way to configure this in the GUI, it is always set to `unicast`.
Thus, if you're running this resource against PAN-OS 8.0+, the appropriate
thing to do is set this value to `unicast` as well to match the GUI functionality.

`AddressPrefixes` - (Optional) List of matching address prefixes.

`NextHops` - (Optional) List of next hop attributes.

`FromPeers` - (Optional) List of peers that advertised the route entry.


## See Also

* [panos_panorama_bgp_conditional_adv_non_exist_filter](https://www.terraform.io/docs/providers/panos/r/panorama_bgp_conditional_adv_non_exist_filter.html) in the _Terraform Provider Documentation_