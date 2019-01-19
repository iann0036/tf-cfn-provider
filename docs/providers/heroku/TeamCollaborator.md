# Terraform::Heroku::TeamCollaborator

Provides a [Heroku Team Collaborator](https://devcenter.heroku.com/articles/platform-api-reference#team-app-collaborator)
resource.

A team collaborator represents an account that has been given access to a team app on Heroku.

~> **NOTE:** Please only use this resource if you have team/organization apps

## Properties

`App` - (Required) The name of the team app that the team collaborator will be added to.

`Email` - (Required) Email address of the team collaborator.

`Permissions` - (Required) List of permissions that will be granted to the team collaborator. The order in which individual permissions are set here does not matter. Please [visit this link](https://devcenter.heroku.com/articles/app-permissions) for more information on available permissions.


## Return Values

### Fn::GetAtt

`Id` - The ID of the team collaborator.

## See Also

* [heroku_team_collaborator](https://www.terraform.io/docs/providers/heroku/r/team_collaborator.html) in the _Terraform Provider Documentation_