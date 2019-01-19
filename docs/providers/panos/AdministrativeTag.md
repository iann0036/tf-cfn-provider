# Terraform::Panos::AdministrativeTag

This resource allows you to add/update/delete administrative tags.

## Properties

`Name` - (Required) The administrative tag's name.

`Vsys` - (Optional) The vsys to put the administrative tag into (default: `vsys1`).

`Color` - (Optional) The tag's color.  This should be either an empty string (no color) or a string such as `color1` or `color15`.  Note that for maximum portability, you should limit color usage to `color16`, which was available in PAN-OS 6.1.  PAN-OS 8.1's colors go up to `color42`.  The value `color18` is reserved internally by PAN-OS and thus not available for use.

`Comment` - (Optional) The administrative tag's description.


## See Also

* [panos_administrative_tag](https://www.terraform.io/docs/providers/panos/r/administrative_tag.html) in the _Terraform Provider Documentation_