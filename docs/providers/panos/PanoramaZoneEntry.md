# Terraform::Panos::PanoramaZoneEntry

This resource allows you to add/update/delete a specific interface in a Panorama
zone.

This resource has some overlap with the `panos_panorama_zone`
resource.  If you want to use this resource with the other one, then make
sure that your `panos_panorama_zone` spec does not define the
`interfaces` field.

This is the appropriate resource to use if you have a pre-existing zone
in Panorama and don't want Terraform to delete it on `terraform destroy`.

## Properties

TBC

## See Also

* [panos_panorama_zone_entry](https://www.terraform.io/docs/providers/panos/r/panorama_zone_entry.html) in the _Terraform Provider Documentation_