# Terraform::Panos::SecurityPolicy

This resource allows you to manage the full security posture.

~> **Note:** `Terraform::Panos::SecurityPolicies` is known as `panosSecurityPolicy`.

This resource manages the full set of security rules in a vsys, enforcing both
the contents of individual rules as well as their ordering.  Rules are defined
in a `Rule` config block.

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

`Vsys` - (Optional) The vsys to put the security policy into (default: `vsys1`).

`Rulebase` - (Optional, Deprecated) The rulebase.  For firewalls, there is only the `Rulebase` value (default), but on Panorama, there is also `pre-rulebase` and `post-rulebase`.

`Rule` - A security rule definition (see below).  The security rule ordering will match how they appear in the terraform plan file.

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

`Schedule` - (Optional) The security policy schedule.

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

* [panos_security_policy](https://www.terraform.io/docs/providers/panos/r/security_policy.html) in the _Terraform Provider Documentation_