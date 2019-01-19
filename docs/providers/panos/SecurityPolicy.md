# Terraform::Panos::SecurityPolicy

This resource allows you to manage the full security posture.

~> **Note:** `panos_security_policies` is known as `panos_security_policy`.

This resource manages the full set of security rules in a vsys, enforcing both
the contents of individual rules as well as their ordering.  Rules are defined
in a `rule` config block.

For each security rule, there are three styles of profile settings:

* `None` (the default)
* `Group`
* `Profiles`

The Profile Setting is implicitly chosen based on what params are configured
for the security rule.  If you want a Profile Setting of `Group`, then the
`group` param should be set to the desired Group Profile.  If you want a
Profile Setting of `Profiles`, then you will need to specify one or more of
the following params:

* `virus`
* `spyware`
* `vulnerability`
* `url_filtering`
* `file_blocking`
* `wildfire_analysis`
* `data_filtering`

If the `group` param and none of the `Profiles` params are specified, then
the Profile Setting is set to `None`.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [panos_security_policy](https://www.terraform.io/docs/providers/panos/r/security_policy.html) in the _Terraform Provider Documentation_