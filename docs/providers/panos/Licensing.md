# Terraform::Panos::Licensing

This resource manages the licenses installed on the PAN-OS firewall.

Installing the standard auth code for the standard PAN-OS license key for the
firewall causes the firewall to reboot.  Thus it is recommended that you use
this resource in a separate step of your overall firewall provisioning, as
using this resource will cause the firewall to be temporarily inaccessible.

## Properties

`AuthCodes` - (Required) The list of auth codes to install.

`Delicense` - (Optional, bool) Leave as `true` if you want to delicense
the firewall when this resource is removed, otherwise set to `false` to
prevent firewall delicensing.  Delicensing requires that the licensing
API key has been installed.

`Mode` - (Optional) For `Delicense` of `true`, the type of delicensing to
perform.  Right now, only `auto` is supported (no manual delicensing).


## See Also

* [panos_licensing](https://www.terraform.io/docs/providers/panos/r/licensing.html) in the _Terraform Provider Documentation_