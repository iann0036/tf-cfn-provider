# Terraform::CLC::PublicIp

Manages a CLC public ip (for an existing server).

See also [Complete API documentation](https://www.ctl.io/api-docs/v2/#public-ip).

## Properties

`ServerId` - (Required, string) The name or ID of the server to bind IP to.

`InternalIpAddress` - (Required, string) The internal IP of the
NIC to attach to. If not provided, a new internal NIC will be
provisioned and used.

`Ports` - (Optional) See [Ports](#ports) below for details.

`SourceRestrictions` - (Optional) See
[SourceRestrictions](#source_restrictions) below for details.


## See Also

* [clc_public_ip](https://www.terraform.io/docs/providers/clc/r/public_ip.html) in the _Terraform Provider Documentation_