# Terraform::GitHub::TeamRepository

This resource manages relationships between teams and repositories
in your GitHub organization.

Creating this resource grants a particular team permissions on a
particular repository.

The repository and the team must both belong to the same organization
on GitHub. This resource does not actually *create* any repositories;
to do that, see [`github_repository`](repository.html).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [github_team_repository](https://www.terraform.io/docs/providers/github/r/team_repository.html) in the _Terraform Provider Documentation_