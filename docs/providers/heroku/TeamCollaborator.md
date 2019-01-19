# Terraform::Heroku::TeamCollaborator

Provides a [Heroku Team Collaborator](https://devcenter.heroku.com/articles/platform-api-reference#team-app-collaborator)
resource.

A team collaborator represents an account that has been given access to a team app on Heroku.

~> **NOTE:** Please only use this resource if you have team/organization apps

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the team collaborator.

## See Also

* [heroku_team_collaborator](https://www.terraform.io/docs/providers/heroku/r/team_collaborator.html) in the _Terraform Provider Documentation_