# Terraform::GitHub::TeamMembership

Provides a GitHub team membership resource.

This resource allows you to add/remove users from teams in your organization. When applied,
the user will be added to the team. If the user hasn't accepted their invitation to the
organization, they won't be part of the team until they do. When
destroyed, the user will be removed from the team.

## Properties

TBC

## See Also

* [github_team_membership](https://www.terraform.io/docs/providers/github/r/team_membership.html) in the _Terraform Provider Documentation_