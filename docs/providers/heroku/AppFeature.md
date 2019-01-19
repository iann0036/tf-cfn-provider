# Terraform::Heroku::AppFeature

Provides a Heroku App Feature resource. This can be used to create and manage App Features on Heroku.

## Properties

`App` - (Required) The Heroku app to link to.

`Name` - (Required) The name of the App Feature to manage.

`Enabled` - (Optional) Whether to enable or disable the App Feature. The default value is true.


## See Also

* [heroku_app_feature](https://www.terraform.io/docs/providers/heroku/r/app_feature.html) in the _Terraform Provider Documentation_