# Terraform::Heroku::TeamMember

Provides a [Heroku Team Collaborator](https://devcenter.heroku.com/articles/platform-api-reference#team-member) resource.

~> **NOTE:** Please only use this resource if you have team/organization apps

## Properties

`Team` - (Required) The name of the Heroku team that the team member will be added to.

`Email` - (Required) Email address of the team collaborator.

`Role` - (Required) The role to assign the team member. See [the API docs](https://devcenter.heroku.com/articles/platform-api-reference#team-member) for available options.


## See Also

* [heroku_team_member](https://www.terraform.io/docs/providers/heroku/r/team_member.html) in the _Terraform Provider Documentation_