# Terraform::GitHub::Team

Provides a GitHub team resource.

This resource allows you to add/remove teams from your organization. When applied,
a new team will be created. When destroyed, that team will be removed.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the created team.

`Slug` - The slug of the created team, which may or may not differ from `name`,.

## See Also

* [github_team](https://www.terraform.io/docs/providers/github/r/team.html) in the _Terraform Provider Documentation_