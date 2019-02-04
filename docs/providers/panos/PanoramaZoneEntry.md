# Terraform::Panos::PanoramaZoneEntry

This resource allows you to add/update/delete a specific interface in a Panorama
zone.

This resource has some overlap with the `Terraform::Panos::PanoramaZone`
resource.  If you want to use this resource with the other one, then make
sure that your `Terraform::Panos::PanoramaZone` spec does not define the
`interfaces` field.

This is the appropriate resource to use if you have a pre-existing zone
in Panorama and don't want Terraform to delete it on `terraform destroy`.

## Properties

`Template` - (Required) The template name.

`Vsys` - (Optional) The vsys (default: `vsys1`).

`Zone` - (Required) The zone's name.

`Mode` - (Optional) The mode.  Can be `layer3` (default), `layer2`,
`virtual-wire`, `tap`, or `external`.

`Interface` - (Required) The interface's name.


## See Also

* [panos_panorama_zone_entry](https://www.terraform.io/docs/providers/panos/r/panorama_zone_entry.html) in the _Terraform Provider Documentation_