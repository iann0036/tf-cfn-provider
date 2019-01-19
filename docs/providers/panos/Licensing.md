# Terraform::Panos::Licensing

This resource manages the licenses installed on the PAN-OS firewall.

Installing the standard auth code for the standard PAN-OS license key for the
firewall causes the firewall to reboot.  Thus it is recommended that you use
this resource in a separate step of your overall firewall provisioning, as
using this resource will cause the firewall to be temporarily inaccessible.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [panos_licensing](https://www.terraform.io/docs/providers/panos/r/licensing.html) in the _Terraform Provider Documentation_