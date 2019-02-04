# Terraform::Panos::BgpRedistRule

This resource allows you to add/update/delete a BGP redistribution rule.

## Properties

`VirtualRouter` - (Required) The virtual router to add this BGP
redist rule to.

`Name` - (Required) A subnet or a redistribution profile.

`Enable` - (Optional, bool) Enable this rule or not (default: `true`).

`AddressFamily` - (Optional) The address family.  Valid values are
`ipv4` (default) or `ipv6`.

`RouteTable` - (Optional, PAN-OS 8.0+) Route table to match rule.  Valid
values are `unicast`, `multicast`, or `both`.  As of PAN-OS 8.1, there doesn't
seem to be a way to configure this in the GUI, it is always set to `unicast`.
Thus, if you're running this resource against PAN-OS 8.0+, the appropriate
thing to do is set this value to `unicast` as well to match the GUI functionality.

`Metric` - (Optional, int) Metric value.

`SetOrigin` - (Optional) Add the origin path attribute.  Valid values are
`incomplete` (default), `igp`, or `egp`.

`SetMed` - (Optional) Add the MULTI_EXIT_DISC path attribute.

`SetLocalPreference` - (Optional) Add the LOCAL_PREF path attribute.

`SetAsPathLimit` - (Optional, int) Add the AS_PATHLIMIT path attribute.

`SetCommunities` - (Optional) List of COMMUNITY path attributes to add.

`SetExtendedCommunities` - (Optional) List of EXTENDED COMMUNITY path attributes to add.


## See Also

* [panos_bgp_redist_rule](https://www.terraform.io/docs/providers/panos/r/bgp_redist_rule.html) in the _Terraform Provider Documentation_