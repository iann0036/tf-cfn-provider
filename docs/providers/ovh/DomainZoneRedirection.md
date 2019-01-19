# Terraform::OVH::DomainZoneRedirection

Provides a OVH domain zone redirection.

## Properties

`Zone` - (Required) The domain to add the redirection to.

`Subdomain` - (Optional) The name of the redirection.

`Target` - (Required) The value of the redirection.

`Type` - (Required) The type of the redirection, with values: * `Visible` -> Redirection by http code 302 * `VisiblePermanent` -> Redirection by http code 301 * `Invisible` -> Redirection by html frame.

`Description` - (Optional) A description of this redirection.

`Keywords` - (Optional) Keywords to describe this redirection.

`Title` - (Optional) Title of this redirection.


## Return Values

### Fn::GetAtt

`Id` - The redirection ID.

`Zone` - The domain to add the redirection to.

`SubDomain` - The name of the redirection.

`Target` - The value of the redirection.

`Type` - The type of the redirection.

`Description` - The description of the redirection.

`Keywords` - Keywords  of the redirection.

`Title` - The title of the redirection.

## See Also

* [ovh_domain_zone_redirection](https://www.terraform.io/docs/providers/ovh/r/domain_zone_redirection.html) in the _Terraform Provider Documentation_