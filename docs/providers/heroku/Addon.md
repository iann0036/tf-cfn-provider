# Terraform::Heroku::Addon

Provides a Heroku Add-On resource. These can be attach
services to a Heroku app.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the add-on.

`Name` - The add-on name.

`Plan` - The plan name.

`ProviderId` - The ID of the plan provider.

`ConfigVars` - The Configuration variables of the add-on.

## See Also

* [heroku_addon](https://www.terraform.io/docs/providers/heroku/r/addon.html) in the _Terraform Provider Documentation_