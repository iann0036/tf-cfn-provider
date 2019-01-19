# Terraform::Panos::GeneralSettings

This resource allows you to update the general device settings, such as DNS
or the hostname.

All params are optional for this resource.  If any options are not specified,
then whatever is already configured on the firewall is left as-is.  The
general device settings will always exist on the firewall, so `terraform
destroy` does not remove config from the firewall.

## Properties

TBC

## See Also

* [panos_general_settings](https://www.terraform.io/docs/providers/panos/r/general_settings.html) in the _Terraform Provider Documentation_