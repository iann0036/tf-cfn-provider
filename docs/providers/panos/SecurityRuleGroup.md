# Terraform::Panos::SecurityRuleGroup

This resource allows you to add/update/delete security rule groups.

~> **Note:** `Terraform::Panos::SecurityPolicyGroup` is known as `panosSecurityRuleGroup`.

This resource manages clusters of security rules in a single vsys,
enforcing both the contents of individual rules as well as their
ordering.  Rules are defined in a `Rule` config block.

Because this resource only manages what it's told to, it will not manage
any rules that may already exist on the firewall.  This has
implications on the effective security posture of your firewall, but it
will allow you to spread your security rules across multiple Terraform
state files.  If you want to verify that the security rules are only
what appears in the plan file, then you should probably be using the
[panos_security_policy](security_policy.html) resource.

Although you cannot modify non-group security rules with this
resource, the `PositionKeyword` and `PositionReference` parameters allow you
to reference some other security rule that already exists, using it as
a means to ensure some rough placement within the ruleset as a whole.

For each security rule, there are three styles of profile settings:

* `None` (the default)
* `Group`
* `Profiles`

The Profile Setting is implicitly chosen based on what params are configured
for the security rule.  If you want a Profile Setting of `Group`, then the
`Group` param should be set to the desired Group Profile.  If you want a
Profile Setting of `Profiles`, then you will need to specify one or more of
the following params:

* `Virus`
* `Spyware`
* `Vulnerability`
* `UrlFiltering`
* `FileBlocking`
* `WildfireAnalysis`
* `DataFiltering`

If the `Group` param and none of the `Profiles` params are specified, then
the Profile Setting is set to `None`.

## Properties

`Vsys` - (Optional) The vsys to put the security rule into (default: `vsys1`).

`PositionKeyword` - (Optional) A positioning keyword for this group.  This can be `before`, `directly before`, `after`, `directly after`, `top`, `bottom`, or left empty (the default) to have no particular placement.  This param works in combination with the `PositionReference` param.

`PositionReference` - (Optional) Required if `PositionKeyword` is one of the "above" or "below" variants, this is the name of a non-group rule to use as a reference to place this group.

`Rule` - The security rule definition (see below).  The security rule ordering will match how they appear in the terraform plan file.

### Rule Properties

`Name` - (Required) The security rule name.

`Type` - (Optional) Rule type.  This can be `universal` (default), `interzone`, or `intrazone`.

`Description` - (Optional) The description.

`Tags` - (Optional) List of tags for this security rule.

`SourceZones` - (Required) List of source zones.

`SourceAddresses` - (Required) List of source addresses.

`NegateSource` - (Optional, bool) If the source should be negated.

`SourceUsers` - (Required) List of source users.

`HipProfiles` - (Required) List of HIP profiles.

`DestinationZones` - (Required) List of destination zones.

`DestinationAddresses` - (Required) List of destination addresses.

`NegateDestination` - (Optional, bool) If the destination should be negated.

`Applications` - (Required) List of applications.

`Services` - (Required) List of services.

`Categories` - (Required) List of categories.

`Action` - (Optional) Action for the matched traffic.  This can be `allow` (default), `deny`, `drop`, `reset-client`, `reset-server`, or `reset-both`.

`LogSetting` - (Optional) Log forwarding profile.

`LogStart` - (Optional, bool) Log the start of the traffic flow.

`LogEnd` - (Optional, bool) Log the end of the traffic flow (default: `true`).

`Disabled` - (Optional, bool) Set to `true` to disable this rule.

`Schedule` - (Optional) The security rule schedule.

`IcmpUnreachable` - (Optional) Set to `true` to enable ICMP unreachable.

`DisableServerResponseInspection` - (Optional) Set to `true` to disable server response inspection.

`Group` - (Optional) Profile Setting: `Group` - The group profile name.

`Virus` - (Optional) Profile Setting: `Profiles` - The antivirus setting.

`Spyware` - (Optional) Profile Setting: `Profiles` - The anti-spyware setting.

`Vulnerability` - (Optional) Profile Setting: `Profiles` - The Vulnerability Protection setting.

`UrlFiltering` - (Optional) Profile Setting: `Profiles` - The URL filtering setting.

`FileBlocking` - (Optional) Profile Setting: `Profiles` - The file blocking setting.

`WildfireAnalysis` - (Optional) Profile Setting: `Profiles` - The WildFire Analysis setting.

`DataFiltering` - (Optional) Profile Setting: `Profiles` - The Data Filtering setting.


## See Also

* [panos_security_rule_group](https://www.terraform.io/docs/providers/panos/r/security_rule_group.html) in the _Terraform Provider Documentation_