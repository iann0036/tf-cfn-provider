# Terraform::GitHub::Team

Provides a GitHub team resource.

This resource allows you to add/remove teams from your organization. When applied,
a new team will be created. When destroyed, that team will be removed.

## Properties

`Name` - (Required) The name of the team.

`Description` - (Optional) A description of the team.

`Privacy` - (Optional) The level of privacy for the team. Must be one of `secret` or `closed`.
Defaults to `secret`.

`ParentTeamId` - (Optional) The ID of the parent team, if this is a nested team.

`LdapDn` - (Optional) The LDAP Distinguished Name of the group where membership will be synchronized. Only available in GitHub Enterprise.


## Return Values

### Fn::GetAtt

`Id` - The ID of the created team.

`Slug` - The slug of the created team, which may or may not differ from `Name`,.

## See Also

* [github_team](https://www.terraform.io/docs/providers/github/r/team.html) in the _Terraform Provider Documentation_