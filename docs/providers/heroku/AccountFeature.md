# Terraform::Heroku::AccountFeature

Provides a Heroku Account Feature resource. An account feature represents a Heroku labs capability
that can be enabled or disabled for an account on Heroku.

~> **NOTE:** If this resource's HCL is removed from a `.tf` file, the behavior is to disable account feature
and remove resource from state.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - Comprised of acount email & feature name.

`Description` - Description of account feature.

`State` - State of account feature.

## See Also

* [heroku_account_feature](https://www.terraform.io/docs/providers/heroku/r/account_feature.html) in the _Terraform Provider Documentation_