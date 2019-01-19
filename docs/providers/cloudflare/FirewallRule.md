# Terraform::Cloudflare::FirewallRule

Define Firewall rules using filter expressions for more control over how traffic is matched to the rule.
A filter expression permits selecting traffic by multiple criteria allowing greater freedom in rule creation.

Filter expressions needs to be created first before using Firewall Rule. See [Filter](filter.html).

## Properties

`Zone` - (Optional) The DNS zone to which the Firewall Rule should be added. Will be resolved to `ZoneId` upon creation.

`ZoneId` - (Optional) The DNS zone to which the Filter should be added.

`Action` - (Required) The action to apply to a matched request. Allowed values: "block", "challenge", "allow", "js_challenge".

`Priority` - (Optional) The priority of the rule to allow control of processing order. A lower number indicates high priority. If not provided, any rules with a priority will be sequenced before those without.

`Paused` - (Optional) Whether this filter based firewall rule is currently paused. Boolean value.

`Expression` - (Required) The filter expression to be used.

`Description` - (Optional) A description of the rule to help identify it.


## Return Values

### Fn::GetAtt

`Id` - Firewall Rule identifier.

`ZoneId` - The DNS zone ID.

## See Also

* [cloudflare_firewall_rule](https://www.terraform.io/docs/providers/cloudflare/r/firewall_rule.html) in the _Terraform Provider Documentation_