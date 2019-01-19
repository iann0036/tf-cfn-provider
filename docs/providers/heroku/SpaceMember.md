# Terraform::Heroku::SpaceMember

Provides a Heroku Space resource for managing app permissions for the entire space. Members with the admin role will always have full permissions to a Heroku Space, so using this resource on an admin will have no affect. The provided member must already exist in your Heroku organization. Currently the only supported permission is `create_apps`.

## Properties

`Space` - (Required) The name of the space.

`Email` - (Required) The email of the team member to set permissions for.

`Permissions` - (Required) The permissions to grant the team member for the space. Currently `create_apps` is the only supported permission. If not provided the member will have no permissions to the space. Members with admin role will always have `create_apps` permissions, which cannot be removed.


## See Also

* [heroku_space_member](https://www.terraform.io/docs/providers/heroku/r/space_member.html) in the _Terraform Provider Documentation_