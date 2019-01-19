# Terraform::Panos::PanoramaDeviceGroup

This resource allows you to add/update/delete Panorama device groups.

This resource has some overlap with the `panos_panorama_device_group_entry`
resource.  If you want to use this resource with the other one, then make
sure that your `panos_panorama_device_group` spec does not define any
`device` blocks, and just stays as "computed".

This is the appropriate resource to use if `terraform destroy` should delete
the device group.

## Properties

TBC

## See Also

* [panos_panorama_device_group](https://www.terraform.io/docs/providers/panos/r/panorama_device_group.html) in the _Terraform Provider Documentation_