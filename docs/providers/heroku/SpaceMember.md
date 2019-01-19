# Terraform::Heroku::SpaceMember

Provides a Heroku Space resource for managing app permissions for the entire space. Members with the admin role will always have full permissions to a Heroku Space, so using this resource on an admin will have no affect. The provided member must already exist in your Heroku organization. Currently the only supported permission is `create_apps`.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [heroku_space_member](https://www.terraform.io/docs/providers/heroku/r/space_member.html) in the _Terraform Provider Documentation_