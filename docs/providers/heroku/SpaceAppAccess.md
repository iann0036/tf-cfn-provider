# Terraform::Heroku::SpaceAppAccess

Provides a resource for managing permissions for the entire Private Space. Members with the admin role will always have full permissions in the Private Space, so using this resource on an admin will have no effect. The provided email must already be a member of the Heroku Team. Currently the only supported permission is `create_apps`.

## Properties

`Space` - (Required) The name of the Private Space.

`Email` - (Required) The email of the existing Heroku Team member.

`Permissions` - (Required) The permissions to grant the team member for the Private Space. Currently `create_apps` is the only supported permission. If not provided the member will have no permissions to the space. Members with admin role will always have `create_apps` permissions, which cannot be removed.


## See Also

* [heroku_space_app_access](https://www.terraform.io/docs/providers/heroku/r/space_app_access.html) in the _Terraform Provider Documentation_