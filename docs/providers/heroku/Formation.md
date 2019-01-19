# Terraform::Heroku::Formation

Provides a [Heroku Formation](https://devcenter.heroku.com/articles/platform-api-reference#formation)
resource.

A formation represents the formation of processes that should be set for an application.

~> **NOTE:** 
- The application must have a dyno in order to update its formation.
- If the heroku formation resource is removed and deleted, this will be a no-op action in Heroku.
The Heroku Platform does not have a `DELETE` endpoint for `formation`.
- This resource works well with the `Terraform::Heroku::AppRelease` resource, which allows you to deploy a slug/release to an application
before the formation can be updated.

## Properties

`App` - (Required) The name of the application.

`Type` - (Required) type of process such as "web".

`Quantity` - (Required) number of processes to maintain.

`Size` - (Required) dyno size (Example: “standard-1X”). Capitalization does not matter.


## Return Values

### Fn::GetAtt

`Id` - The ID of the formation.

## See Also

* [heroku_formation](https://www.terraform.io/docs/providers/heroku/r/formation.html) in the _Terraform Provider Documentation_