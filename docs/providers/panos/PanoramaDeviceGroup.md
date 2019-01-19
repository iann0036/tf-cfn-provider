# Terraform::Panos::PanoramaDeviceGroup

This resource allows you to add/update/delete Panorama device groups.

This resource has some overlap with the `Terraform::Panos::PanoramaDeviceGroupEntry`
resource.  If you want to use this resource with the other one, then make
sure that your `Terraform::Panos::PanoramaDeviceGroup` spec does not define any
`Device` blocks, and just stays as "computed".

This is the appropriate resource to use if `terraform destroy` should delete
the device group.

## Properties

`Name` - (Required) The device group's name.

`Description` - (Optional) The device group's description.

`Device` - The device definition (see below).

### Device Properties

`Serial` - (Required) The serial number of the firewall.

`VsysList` - (Optional) A subset of all available vsys on the firewall that should be in this device group.  If the firewall is a virtual firewall, then this parameter should just be omitted.


## See Also

* [panos_panorama_device_group](https://www.terraform.io/docs/providers/panos/r/panorama_device_group.html) in the _Terraform Provider Documentation_