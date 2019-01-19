# Terraform::Heroku::App

Provides a Heroku App resource. This can be used to
create and manage applications on Heroku.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the app. This is also the name of the application.

`Name` - The name of the application. In Heroku, this is also the.

`Stack` - The application stack is what platform to run the application.

`Space` - The private space the app should run in.

`InternalRouting` - Whether internal routing is enabled the private space.

`Region` - The region that the app should be deployed in.

`GitUrl` - The Git URL for the application. This is used for.

`WebUrl` - The web (HTTP) URL that the application can be accessed.

`HerokuHostname` - A hostname for the Heroku application, suitable.

`AllConfigVars` - A map of all of the configuration variables that.

`Uuid` - The unique UUID of the Heroku app. **NOTE:** Use this for `null_resource` triggers.

## See Also

* [heroku_app](https://www.terraform.io/docs/providers/heroku/r/app.html) in the _Terraform Provider Documentation_