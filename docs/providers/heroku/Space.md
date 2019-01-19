# Terraform::Heroku::Space

Provides a Heroku Space resource for running apps in isolated, highly available, secure app execution environments.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the space.

`Name` - The space's name.

`Organization` - The space's organization.

`Region` - The space's region.

`OutboundIps` - The space's stable outbound [NAT IPs](https://devcenter.heroku.com/articles/platform-api-reference#space-network-address-translation).

## See Also

* [heroku_space](https://www.terraform.io/docs/providers/heroku/r/space.html) in the _Terraform Provider Documentation_