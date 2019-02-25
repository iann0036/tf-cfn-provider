# Terraform::Heroku::AccountFeature

This resource is used to create and manage [User Features](https://devcenter.heroku.com/articles/heroku-beta-features) on Heroku.

~> **NOTE:** If this resource's HCL is removed from a `.tf` file, the behavior is to disable account feature
and remove resource from state.

## Properties

`Name` - (Required) Name of the account feature.

`Enabled` - (Required) Enable or disable the account feature.


## Return Values

### Fn::GetAtt

`Id` - Comprised of acount email & feature name.

`Description` - Description of account feature.

`State` - State of account feature.

## See Also

* [heroku_account_feature](https://www.terraform.io/docs/providers/heroku/r/account_feature.html) in the _Terraform Provider Documentation_