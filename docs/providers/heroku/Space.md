# Terraform::Heroku::Space

Provides a Heroku Space resource for running apps in isolated, highly available, secure app execution environments.

## Properties

`Name` - (Required) The name of the space.

`Organization` - (Required) The name of the organization which will own the space.

`Region` - (Optional) The region that the space should be created in.

`Shield` - (Optional) Whether or not the private space should be [shielded](https://devcenter.heroku.com/articles/private-spaces#shield-private-spaces).


## Return Values

### Fn::GetAtt

`Id` - The ID of the space.

`Name` - The space's name.

`Organization` - The space's organization.

`Region` - The space's region.

`OutboundIps` - The space's stable outbound [NAT IPs](https://devcenter.heroku.com/articles/platform-api-reference#space-network-address-translation).

## See Also

* [heroku_space](https://www.terraform.io/docs/providers/heroku/r/space.html) in the _Terraform Provider Documentation_