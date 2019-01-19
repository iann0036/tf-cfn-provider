# Terraform::Heroku::Addon

Provides a Heroku Add-On resource. These can be attach
services to a Heroku app.

## Properties

`App` - (Required) The Heroku app to add to.

`Plan` - (Required) The addon to add.

`Config` - (Optional) Optional plan configuration.


## Return Values

### Fn::GetAtt

`Id` - The ID of the add-on.

`Name` - The add-on name.

`Plan` - The plan name.

`ProviderId` - The ID of the plan provider.

`ConfigVars` - The Configuration variables of the add-on.

## See Also

* [heroku_addon](https://www.terraform.io/docs/providers/heroku/r/addon.html) in the _Terraform Provider Documentation_