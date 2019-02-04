# Terraform::PagerDuty::Team

A [team](https://v2.developer.pagerduty.com/v2/page/api-reference#!/Teams/get_teams) is a collection of users and escalation policies that represent a group of people within an organization.

The account must have the `teams` ability to use the following resource.

## Properties

`Name` - (Required) The name of the group.

`Description` - (Optional) A human-friendly description of the team.
If not set, a placeholder of "Managed by Terraform" will be set.


## Return Values

### Fn::GetAtt

`Id` - The ID of the team.

## See Also

* [pagerduty_team](https://www.terraform.io/docs/providers/pagerduty/r/team.html) in the _Terraform Provider Documentation_