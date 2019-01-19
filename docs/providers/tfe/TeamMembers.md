# Terraform::Tfe::TeamMembers

Manages users in a team.

~> **NOTE** on managing team memberships: Terraform currently provides two
resources for managing team memberships. The [tfe_team_member](team_member.html)
resource can be used multiple times as it manages the team membership for a
single user.  The [tfe_team_members](team_members.html) resource, on the other
hand, is used to manage all team memberships for a specific team and can only be
used once. Both resources cannot be used for the same team simultaneously.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the team.

## See Also

* [tfe_team_members](https://www.terraform.io/docs/providers/tfe/r/team_members.html) in the _Terraform Provider Documentation_