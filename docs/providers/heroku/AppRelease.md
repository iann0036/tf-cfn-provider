# Terraform::Heroku::AppRelease

Provides a [Heroku App Release](https://devcenter.heroku.com/articles/platform-api-reference#release)
resource.

An app release represents a combination of code, config vars and add-ons for an app on Heroku.

~> **NOTE:** This resource requires the slug be uploaded to Heroku using [`heroku_slug`](slug.html) or with external tooling prior to running terraform.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the app release.

## See Also

* [heroku_app_release](https://www.terraform.io/docs/providers/heroku/r/app_release.html) in the _Terraform Provider Documentation_