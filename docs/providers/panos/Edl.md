# Terraform::Panos::Edl

This resource allows you to add/update/delete external dynamic lists (EDL).

## Properties

`Name` - (Required) The object's name.

`Vsys` - (Optional) The vsys to put the object into (default: `vsys1`).

`Type` - (Optional) The type of EDL.  This can be `ip` (the default; and the only valid value for PAN-OS 6.1 - 7.0), `domain`, `url`, or `predefined` (PAN-OS 8.0+).

`Description` - (Optional) The object's description.

`Source` - (Optional) The EDL source URL.

`CertificateProfile` - (Optional) Profile for authenticating client certificates.

`Username` - (Optional) EDL username.

`Password` - (Optional) EDL password.

`Repeat` - (Optional) How often to retrieve the EDL.  This can be `hourly` (the default), `daily`, `weekly`, `monthly`, or `every five minutes` (valid for PAN-OS 7.1+).

`RepeatAt` - (Optional) The time at which to retrieve the EDL.  Please refer to the section above for how to set this value properly.

`RepeatDayOfWeek` - (Optional) If `Repeat` is `weekly`, then this should be set to the desired day of the week.  Valid values are `sunday`, `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday`, and `sunday`.

`RepeatDayOfMonth` - (Optional, int) If `Repeat` is `monthly`, then this should be set to the desired day of the month.

`Exceptions` - (Optional, list) Provide a list of exception entries.


## See Also

* [panos_edl](https://www.terraform.io/docs/providers/panos/r/edl.html) in the _Terraform Provider Documentation_