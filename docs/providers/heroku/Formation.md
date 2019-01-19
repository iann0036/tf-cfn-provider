# Terraform::Heroku::Formation

Provides a [Heroku Formation](https://devcenter.heroku.com/articles/platform-api-reference#formation)
resource.

A formation represents the formation of processes that should be set for an application.

~> **NOTE:** 
- The application must have a dyno in order to update its formation.
- If the heroku formation resource is removed and deleted, this will be a no-op action in Heroku.
The Heroku Platform does not have a `DELETE` endpoint for `formation`.
- This resource works well with the `heroku_app_release` resource, which allows you to deploy a slug/release to an application
before the formation can be updated.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the formation.

## See Also

* [heroku_formation](https://www.terraform.io/docs/providers/heroku/r/formation.html) in the _Terraform Provider Documentation_