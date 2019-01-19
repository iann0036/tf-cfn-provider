# Terraform::Panos::Zone

This resource allows you to add/update/delete zones.

This resource has some overlap with the `panos_zone_entry`
resource.  If you want to use this resource with the other one, then make
sure that your `panos_zone` spec does not define the
`interfaces` field.

## Properties

TBC

## See Also

* [panos_zone](https://www.terraform.io/docs/providers/panos/r/zone.html) in the _Terraform Provider Documentation_