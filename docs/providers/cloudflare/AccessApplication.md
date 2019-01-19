# Terraform::Cloudflare::AccessApplication

Provides a Cloudflare Access Application resource. Access Applications
are used to restrict access to a whole application using an
authorisation gateway managed by Cloudflare.

## Properties

`ZoneId` - (Required) The DNS zone to which the access rule should be added.

`Name` - (Required) Friendly name of the Access Application.

`Domain` - (Required) The complete URL of the asset you wish to put Cloudflare Access in front of. Can include subdomains or paths. Or both.

`SessionDuration` - (Optional) How often a user will be forced to re-authorise. Must be one of `30m`, `6h`, `12h`, `24h`, `168h`, `730h`.


## See Also

* [cloudflare_access_application](https://www.terraform.io/docs/providers/cloudflare/r/access_application.html) in the _Terraform Provider Documentation_