# Terraform::Panos::BgpPeerGroup

This resource allows you to add/update/delete a BGP peer group.

## Properties

`VirtualRouter` - (Required) The virtual router to add this BGP
peer group to.

`Name` - (Required) The name.

`Enable` - (Optional, bool) Enable or not (default: `true`).

`AggregatedConfedAsPath` - (Optional, bool) The peers understand aggregated confederation AS path (default: `true`).

`SoftResetWithStoredInfo` - (Optional, bool) Soft reset with stored info.

`Type` - (Optional) Peer group type.  Valid options are `ebgp` (default),
`ebgp-confed`, `ibgp`, or `ibgp-confed`.

`ExportNextHop` - (Optional) Export next hop.  Valid values are
`original`, `use-self`, or `resolve`.

`ImportNextHop` - (Optional) Import next hop.  Valid values are
`original`, `use-peer`, or the empty string.

`RemovePrivateAs` - (Optional, bool) Remove private AS when exporting
route.  Only available for `type=ebgp`.


## See Also

* [panos_bgp_peer_group](https://www.terraform.io/docs/providers/panos/r/bgp_peer_group.html) in the _Terraform Provider Documentation_