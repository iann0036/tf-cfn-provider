# Terraform::Heroku::SpaceInboundRuleset

Provides a resource for managing [inbound rulesets](https://devcenter.heroku.com/articles/platform-api-reference#inbound-ruleset) for Heroku Private Spaces.

## Properties

`Space` - (Required) The name of the space.

`Rule` - (Required) At least one `Rule` block. Rules are documented below.

`Action` - (Required) The action to apply this rule to. Must be one of `allow` or `deny`.

`Source` - (Required) A CIDR block source for the rule.


## Return Values

### Fn::GetAtt

`Id` - The ID of the inbound ruleset.

## See Also

* [heroku_space_inbound_ruleset](https://www.terraform.io/docs/providers/heroku/r/space_inbound_ruleset.html) in the _Terraform Provider Documentation_