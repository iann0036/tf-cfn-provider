# Terraform::Panos::PanoramaBgpImportRuleGroup

This resource allows you to add/update/delete Panorama BGP import rule groups.

This resource manages clusters of import rules in a virtual router,
enforcing both the contents of individual rules as well as their
ordering.  Rules are defined in a `Rule` config block.

Although you cannot modify non-group import rules with this
resource, the `PositionKeyword` and `PositionReference` parameters allow you
to reference some other import rule that already exists, using it as
a means to ensure some rough placement within the ruleset as a whole.

## Properties

`Template` - The template name.

`TemplateStack` - The template stack name.

`VirtualRouter` - (Required) The virtual router to put the rule into.

`PositionKeyword` - (Optional) A positioning keyword for this group.  This
can be `before`, `directly before`, `after`, `directly after`, `top`,
`bottom`, or left empty (the default) to have no particular placement.  This
param works in combination with the `PositionReference` param.

`PositionReference` - (Optional) Required if `PositionKeyword` is one of the
"above" or "below" variants, this is the name of a non-group rule to use
as a reference to place this group.

`Rule` - The import rule definition (see below).  The import rule
ordering will match how they appear in the terraform plan file.

### Rule Properties

`Name` - (Required) The security rule name.

`Enable` - (Optional, bool) Enable this import rule (default: `true`).

`UsedBy` - (Optional) List of auth profiles.

`MatchAsPathRegex` - (Optional) AS path to match.

`MatchCommunityRegex` - (Optional) Community to match.

`MatchExtendedCommunityRegex` - (Optional) Extended community to match.

`MatchMed` - (Optional) Match MED.

`MatchRouteTable` - (Optional, PAN-OS 8.0+) Route table to match rule.  Valid
values are `unicast`, `multicast`, or `both`.  As of PAN-OS 8.1, there doesn't
seem to be a way to configure this in the GUI, it is always set to `unicast`.
Thus, if you're running this resource against PAN-OS 8.0+, the appropriate
thing to do is set this value to `unicast` as well to match the GUI functionality.

`MatchAddressPrefix` - (Optional, repeatable) Matching address prefix definition
(see below).
below for the params for this section.

`MatchNextHops` - (Optional) List of next hop attributes.

`MatchFromPeers` - (Optional) List of peers that advertised the route entry.

`Action` - (Optional) Rule action.  Valid values are `allow` (default) or
`deny`.

`Dampening` - (Optional) Route flap dampening profile.

`LocalPreference` - (Optional) New local preference value.

`Med` - (Optional) New MED value.

`Weight` - (Optional, int) New weight value.

`NextHop` - (Optional) Next hop address.

`Origin` - (Optional) New route origin.  Valid values are `igp`, `egp`, or
`incomplete`.

`AsPathLimit` - (Optional, int) Add AS path limit attribute if it does
not exist.

`AsPathType` - (Optional) AS path update options.  Valid values are
`none` or `remove`.

`CommunityType` - (Optional) Community update options.  Valid values are
`none`, `remove-all`, `remove-regex`, `append`, or `overwrite`.

`CommunityValue` - (Optional) If `CommunityType` is `remove-regex`,
`append`, or `overwrite`, the value associated with that setting.  For the
`append` and `overwrite` types specifically, valid values for `CommunityValue`
are `no-export`, `no-advertise`, `local-as`, or `nopeer`.

`ExtendedCommunityType` - (Optional) Extended community update options.  Valid
values are `none`, `remove-all`, `remove-regex`, `append`, or `overwrite`.

`ExtendedCommunityVaule` - (Optional) If `ExtendedCommunityType` is
`remove-regex`, `append`, or `overwrite`, the value associated with that setting.

### MatchAddressPrefix Properties

`Prefix` - (Required) Address prefix.

`Exact` - (Optional, bool) Match exact prefix length.


## See Also

* [panos_panorama_bgp_import_rule_group](https://www.terraform.io/docs/providers/panos/r/panorama_bgp_import_rule_group.html) in the _Terraform Provider Documentation_