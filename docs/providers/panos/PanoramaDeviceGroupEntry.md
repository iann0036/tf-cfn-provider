# Terraform::Panos::PanoramaDeviceGroupEntry

This resource allows you to add/update/delete a specific device in a Panorama
device group.

This resource has some overlap with the `Terraform::Panos::PanoramaDeviceGroup`
resource.  If you want to use this resource with the other one, then make
sure that your `Terraform::Panos::PanoramaDeviceGroup` spec does not define any
`device` blocks, and just stays as "computed".

This is the appropriate resource to use if you have a pre-existing device group
in Panorama and don't want Terraform to delete it on `terraform destroy`.

An interesting side effect of the underlying XML API - if the device group does
not already exist, then this resource can actually create it.  However, since
only the single entry for the specific serial number is deleted, then a
`terraform destroy` would not remove the device group itself in this situation.

## Properties

`DeviceGroup` - (Required) The device group's name.

`Serial` - (Required) The serial number of the firewall.

`VsysList` - (Optional) A subset of all available vsys on the firewall
that should be in this device group.  If the firewall is a virtual firewall,
then this parameter should just be omitted.


## See Also

* [panos_panorama_device_group_entry](https://www.terraform.io/docs/providers/panos/r/panorama_device_group_entry.html) in the _Terraform Provider Documentation_