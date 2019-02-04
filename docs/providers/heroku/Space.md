# Terraform::Heroku::Space

Provides a Heroku Space resource for running apps in isolated, highly available, secure app execution environments.

## Properties

`Name` - (Required) The name of the space.

`Organization` - (Required) The name of the organization which will own the space.

`Cidr` - (Optional) The RFC-1918 CIDR the Private Space will use. It must be a /16 in 10.0.0.0/8, 172.16.0.0/12 or 192.168.0.0/16.

`DataCidr` - (Optional) The RFC-1918 CIDR that the Private Space will use for the Heroku-managed peering connection that’s automatically created when using Heroku Data add-ons. It must be between a /16 and a /20.

`Region` - (Optional) The region that the space should be created in.

`Shield` - (Optional) Whether or not the private space should be [shielded](https://devcenter.heroku.com/articles/private-spaces#shield-private-spaces).


## Return Values

### Fn::GetAtt

`Id` - The ID of the space.

`Name` - The space's name.

`Organization` - The space's organization.

`Region` - The space's region.

`Cidr` - The space's CIDR.

`DataCidr` - The space's Data CIDR.

`OutboundIps` - The space's stable outbound [NAT IPs](https://devcenter.heroku.com/articles/platform-api-reference#space-network-address-translation).

## See Also

* [heroku_space](https://www.terraform.io/docs/providers/heroku/r/space.html) in the _Terraform Provider Documentation_