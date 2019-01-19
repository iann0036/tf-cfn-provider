# Terraform::Cloudflare::FirewallRule

Define Firewall rules using filter expressions for more control over how traffic is matched to the rule.
A filter expression permits selecting traffic by multiple criteria allowing greater freedom in rule creation.

Filter expressions needs to be created first before using Firewall Rule. See [Filter](filter.html).

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - Firewall Rule identifier.

`ZoneId` - The DNS zone ID.

## See Also

* [cloudflare_firewall_rule](https://www.terraform.io/docs/providers/cloudflare/r/firewall_rule.html) in the _Terraform Provider Documentation_