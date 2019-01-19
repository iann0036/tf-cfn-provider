# Terraform::Panos::PanoramaServiceGroup

This resource allows you to add/update/delete Panorama service groups.

## Properties

`Name` - (Required) The service group's name.

`DeviceGroup` - (Optional) The device group to put the service group into (default: `shared`).

`Services` - (Required) List of services to put in this service group.

`Tags` - (Optional) List of administrative tags.


## See Also

* [panos_panorama_service_group](https://www.terraform.io/docs/providers/panos/r/panorama_service_group.html) in the _Terraform Provider Documentation_