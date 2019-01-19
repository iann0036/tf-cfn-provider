# Terraform::Cloudflare::WafRule

Provides a Cloudflare WAF rule resource for a particular zone. This can be used to configure firewall behaviour for pre-defined firewall rules.

## Properties

`Zone` - (Required) The DNS zone to apply to.

`RuleId` - (Required) The WAF Rule ID.

`Mode` - (Required) The mode of the rule, can be one of ["block", "challenge", "default", "disable, "simulate"].


## Return Values

### Fn::GetAtt

`Id` - The WAF Rule ID, the same as rule_id.

`ZoneId` - The DNS zone ID.

`PackageId` - The ID of the WAF Rule Package that contains the rule.

## See Also

* [cloudflare_waf_rule](https://www.terraform.io/docs/providers/cloudflare/r/waf_rule.html) in the _Terraform Provider Documentation_