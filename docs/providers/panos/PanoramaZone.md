# Terraform::Panos::PanoramaZone

This resource allows you to add/update/delete zones on Panorama for both
templates and template stacks.

This resource has some overlap with the `panos_panorama_zone_entry`
resource.  If you want to use this resource with the other one, then make
sure that your `panos_panorama_zone` spec does not define the
`interfaces` field.

## Properties

TBC

## See Also

* [panos_panorama_zone](https://www.terraform.io/docs/providers/panos/r/panorama_zone.html) in the _Terraform Provider Documentation_