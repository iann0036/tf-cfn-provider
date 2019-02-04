# Terraform::Panos::BgpAggregate

This resource allows you to add/update/delete BGP address aggregation
rules.

## Properties

`VirtualRouter` - (Required) The virtual router to put the rule into.

`Name` - (Required) The rule name.

`Prefix` - (Required) Aggregating address prefix.

`Enable` - (Optional, bool) Enable this rule (default: `true`).

`AsSet` - (Optional, bool) Generate AS-set attribute.

`Summary` - (Optional, bool) Summarize route.

`LocalPreference` - (Optional) New local preference value.

`Med` - (Optional) New MED value.

`Weight` - (Optional, int) New weight value.

`NextHop` - (Optional) Next hop address.

`Origin` - (Optional) New route origin.  Valid values are `incomplete`
(default), `igp`, or `egp`.

`AsPathLimit` - (Optional, int) Add AS path limit attribute if it does
not exist.

`AsPathType` - (Optional) AS path update options.  Valid values are
`none` (default) or `prepend`.

`AsPathValue` - (Optional) For `AsPathType` of `prepend`, the value to
prepend.

`CommunityType` - (Optional) Community update options.  Valid values are
`none` (default), `remove-all`, `remove-regex`, `append`, or `overwrite`.

`CommunityValue` - (Optional) If `CommunityType` is `remove-regex`,
`append`, or `overwrite`, the value associated with that setting.  For the
`append` and `overwrite` types specifically, valid values are
`no-export`, `no-advertise`, `local-as`, or `nopeer`.

`ExtendedCommunityType` - (Optional) Extended community update options.  Valid
values are `none` (default), `remove-all`, `remove-regex`, `append`, or `overwrite`.

`ExtendedCommunityVaule` - (Optional) If `ExtendedCommunityType` is
`remove-regex`, `append`, or `overwrite`, the value associated with that setting.


## See Also

* [panos_bgp_aggregate](https://www.terraform.io/docs/providers/panos/r/bgp_aggregate.html) in the _Terraform Provider Documentation_