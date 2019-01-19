# Terraform::Panos::LicenseApiKey

This resource manages the licensing API key, which is necessary to delicense
the PAN-OS firewall.

This resource's `retain_key` param is a Terraform side configuration only.  In
order for the firewall to delicense itself, the licensing API key must be
present.  This means that either the `panos_licensing` resource must use
`depends_on` and depend on this resource, or you must set the `retain_key`
param to `true`.  As there is no harm in leaving the licensing API key on the
PAN-OS firewall, it is recommended that `retain_key` be set to `true`.

## Properties

TBC

## See Also

* [panos_license_api_key](https://www.terraform.io/docs/providers/panos/r/license_api_key.html) in the _Terraform Provider Documentation_