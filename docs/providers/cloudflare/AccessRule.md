# Terraform::Cloudflare::AccessRule

Provides a Cloudflare IP Firewall Access Rule resource. Access control can be applied on basis of IP addresses, IP ranges, AS numbers or countries.

## Properties

`Zone` - (Optional) The DNS zone to which the access rule should be added. Will be resolved to `ZoneId` upon creation.

`ZoneId` - (Optional) The DNS zone to which the access rule should be added.

`Mode` - (Required) The action to apply to a matched request. Allowed values: "block", "challenge", "whitelist", "js_challenge".

`Notes` - (Optional) A personal note about the rule. Typically used as a reminder or explanation for the rule.

`Configuration` - (Required) Rule configuration to apply to a matched request. It's a complex value. See description below.

`Target` - (Required) The request property to target. Allowed values: "ip", "ip_range", "asn", "country".

`Value` - (Required) The value to target. Depends on target's type.


## Return Values

### Fn::GetAtt

`Id` - The access rule ID.

`ZoneId` - The DNS zone ID.

## See Also

* [cloudflare_access_rule](https://www.terraform.io/docs/providers/cloudflare/r/access_rule.html) in the _Terraform Provider Documentation_