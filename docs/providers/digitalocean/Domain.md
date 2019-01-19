# Terraform::DigitalOcean::Domain

Provides a DigitalOcean domain resource.

## Properties

`Name` - (Required) The name of the domain.

`IpAddress` - (Optional) The IP address of the domain. If specified, this IP is used to created an initial A record for the domain.


## Return Values

### Fn::GetAtt

`Id` - The name of the domain.

## See Also

* [digitalocean_domain](https://www.terraform.io/docs/providers/digitalocean/r/domain.html) in the _Terraform Provider Documentation_