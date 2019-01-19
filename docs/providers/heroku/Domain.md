# Terraform::Heroku::Domain

Provides a Heroku App resource. This can be used to
create and manage applications on Heroku.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the of the domain record.

`Hostname` - The hostname traffic will be served as.

`Cname` - The CNAME traffic should route to.

## See Also

* [heroku_domain](https://www.terraform.io/docs/providers/heroku/r/domain.html) in the _Terraform Provider Documentation_