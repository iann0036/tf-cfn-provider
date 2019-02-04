# Terraform::Gitlab::User

This resource allows you to create and manage GitLab users.
Note your provider will need to be configured with admin-level access for this resource to work.

## Properties

`Name` - (Required) The name of the user.

`Username` - (Required) The username of the user.

`Password` - (Required) The password of the user.

`Email` - (Required) The e-mail address of the user.

`IsAdmin` - (Optional) Boolean, defaults to false.  Whether to enable administrative priviledges
for the user.

`ProjectsLimit` - (Optional) Integer, defaults to 0.  Number of projects user can create.

`CanCreateGroup` - (Optional) Boolean, defaults to false. Whether to allow the user to create groups.

`SkipConfirmation` - (Optional) Boolean, defaults to true. Whether to skip confirmation.

`IsExternal` - (Optional) Boolean, defaults to false. Whether a user has access only to some internal or private projects. External users can only access projects to which they are explicitly granted access.


## Return Values

### Fn::GetAtt

`Id` - The unique id assigned to the user by the GitLab server.

## See Also

* [gitlab_user](https://www.terraform.io/docs/providers/gitlab/r/user.html) in the _Terraform Provider Documentation_