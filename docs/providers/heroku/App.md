# Terraform::Heroku::App

Provides a Heroku App resource. This can be used to
create and manage applications on Heroku.

## Properties

`Name` - (Required) The name of the application. In Heroku, this is also the
unique ID, so it must be unique and have a minimum of 3 characters.

`Region` - (Required) The region that the app should be deployed in.

`Stack` - (Optional) The application stack is what platform to run the application
in.

`Buildpacks` - (Optional) Buildpack names or URLs for the application.
Buildpacks configured externally won't be altered if this is not present.

`ConfigVars` - (Optional) Configuration variables for the application.
The config variables in this map are not the final set of configuration
variables, but rather variables you want present. That is, other
configuration variables set externally won't be removed by Terraform
if they aren't present in this list.

`SensitiveConfigVars` - (Optional) This argument is the same as `ConfigVars`.
The main difference between the two is when `SensitiveConfigVars` outputs
are displayed on-screen following a terraform apply or terraform refresh,
they are redacted, with <sensitive> displayed in place of their value.
It is recommended to put private keys, passwords, etc in this argument.

`Space` - (Optional) The name of a private space to create the app in.

`InternalRouting` - (Optional) If true, the application will be routable
only internally in a private space. This option is only available for apps
that also specify `Space`.

`Organization` - (Optional) A block that can be specified once to define
organization settings for this app. The fields for this block are
documented below.

`Acm` - (Optional) The flag representing Automated Certificate Management for the app.


## Return Values

### Fn::GetAtt

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