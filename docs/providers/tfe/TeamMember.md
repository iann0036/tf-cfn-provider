# Terraform::Tfe::TeamMember

Add or remove a user from a team.

~> **NOTE** on managing team memberships: Terraform currently provides two
resources for managing team memberships. The [tfe_team_member](team_member.html)
resource can be used multiple times as it manages the team membership for a
single user.  The [tfe_team_members](team_members.html) resource, on the other
hand, is used to manage all team memberships for a specific team and can only be
used once. Both resources cannot be used for the same team simultaneously.

## Properties

TBC

## See Also

* [tfe_team_member](https://www.terraform.io/docs/providers/tfe/r/team_member.html) in the _Terraform Provider Documentation_