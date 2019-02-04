# Terraform::Tfe::TeamAccess

Associate a team to permissions on a workspace.

## Properties

`Access` - (Required) Type of access to grant. Valid values are `admin`,
`read`, `plan`, or `write`.

`TeamId` - (Required) ID of the team to add to the workspace.

`WorkspaceId` - (Required) Workspace ID to which the team will be added.


## See Also

* [tfe_team_access](https://www.terraform.io/docs/providers/tfe/r/team_access.html) in the _Terraform Provider Documentation_