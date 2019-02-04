# Terraform::Panos::RedistributionProfileIpv4

This resource allows you to add/update/delete IPv4 redistribution profiles
on a virtual router.

## Properties

`Name` - (Required) The redistribution profile's name.

`VirtualRouter` - (Required) The virtual router to add the
redistribution profile to.

`Priority` - (Required, int) The priority, integer from 1 to 255.

`Action` - (Optional) The action.  Valid values are `redist` (default) or
`no-redist`.

`Types` - (Optional) The source types.  Valid values are `bgp`, `connect`,
`ospf`, `rip`, and `static`.

`Interfaces` - (Optional) Specify candidate routes.

`Destinations` - (Optional) Specify candidate routes' next-hop addresses
(subnet match).

`NextHops` - (Optional) Specify candidate routes' next-hop addresses
(subnet match).

`OspfPathTypes` - (Optional) OSPF path types.  Valid values are
`intra-area`, `inter-area`, `ext-1`, and `ext-2`.

`OspfAreas` - (Optional) OSPF areas.

`OspfTags` - (Optional) OSPF tags.

`BgpCommunities` - (Optional) BGP communities.

`BgpExtendedCommunities` - (Optional) BGP extended communities.


## See Also

* [panos_redistribution_profile_ipv4](https://www.terraform.io/docs/providers/panos/r/redistribution_profile_ipv4.html) in the _Terraform Provider Documentation_