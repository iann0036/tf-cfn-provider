# Terraform::Panos::LicenseApiKey

This resource manages the licensing API key, which is necessary to delicense
the PAN-OS firewall.

This resource's `RetainKey` param is a Terraform side configuration only.  In
order for the firewall to delicense itself, the licensing API key must be
present.  This means that either the `Terraform::Panos::Licensing` resource must use
`depends_on` and depend on this resource, or you must set the `RetainKey`
param to `true`.  As there is no harm in leaving the licensing API key on the
PAN-OS firewall, it is recommended that `RetainKey` be set to `true`.

## Properties

`Key` - (Required) The licensing API key.

`RetainKey` - (Optional) Set to `true` to retain the licensing API key
even after the deletion of this resource (recommended).


## See Also

* [panos_license_api_key](https://www.terraform.io/docs/providers/panos/r/license_api_key.html) in the _Terraform Provider Documentation_