# Terraform::Gitlab::ProjectMembership

This resource allows you to add a current user to an existing project with a set access level.

## Properties

`ProjectId` - (Required) The id of the project.

`UserId` - (Required) The id of the user.

`AccessLevel` - (Required) One of five levels of access to the project.


## See Also

* [gitlab_project_membership](https://www.terraform.io/docs/providers/gitlab/r/project_membership.html) in the _Terraform Provider Documentation_