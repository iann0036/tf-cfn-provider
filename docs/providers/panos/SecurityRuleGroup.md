# Terraform::Panos::SecurityRuleGroup

This resource allows you to add/update/delete security rule groups.

~> **Note:** `panos_security_policy_group` is known as `panos_security_rule_group`.

This resource manages clusters of security rules in a single vsys,
enforcing both the contents of individual rules as well as their
ordering.  Rules are defined in a `rule` config block.

Because this resource only manages what it's told to, it will not manage
any rules that may already exist on the firewall.  This has
implications on the effective security posture of your firewall, but it
will allow you to spread your security rules across multiple Terraform
state files.  If you want to verify that the security rules are only
what appears in the plan file, then you should probably be using the
[panos_security_policy](security_policy.html) resource.

Although you cannot modify non-group security rules with this
resource, the `position_keyword` and `position_reference` parameters allow you
to reference some other security rule that already exists, using it as
a means to ensure some rough placement within the ruleset as a whole.

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

## Properties

TBC

## See Also

* [panos_security_rule_group](https://www.terraform.io/docs/providers/panos/r/security_rule_group.html) in the _Terraform Provider Documentation_