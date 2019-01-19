# Terraform::Heroku::AppRelease

Provides a [Heroku App Release](https://devcenter.heroku.com/articles/platform-api-reference#release)
resource.

An app release represents a combination of code, config vars and add-ons for an app on Heroku.

~> **NOTE:** This resource requires the slug be uploaded to Heroku using [`Terraform::Heroku::Slug`](slug.html) or with external tooling prior to running terraform.

## Properties

`App` - (Required) The name of the application.

`SlugId` - unique identifier of slug.

`Description` - description of changes in this release.


## Return Values

### Fn::GetAtt

`Id` - The ID of the app release.

## See Also

* [heroku_app_release](https://www.terraform.io/docs/providers/heroku/r/app_release.html) in the _Terraform Provider Documentation_