# Terraform::GitHub::TeamRepository

This resource manages relationships between teams and repositories
in your GitHub organization.

Creating this resource grants a particular team permissions on a
particular repository.

The repository and the team must both belong to the same organization
on GitHub. This resource does not actually *create* any repositories;
to do that, see [`Terraform::GitHub::Repository`](repository.html).

## Properties

`TeamId` - (Required) The GitHub team id.

`Repository` - (Required) The repository to add to the team.

`Permission` - (Optional) The permissions of team members regarding the repository. Must be one of `pull`, `push`, or `admin`. Defaults to `pull`.


## See Also

* [github_team_repository](https://www.terraform.io/docs/providers/github/r/team_repository.html) in the _Terraform Provider Documentation_