# Terraform::Panos::PanoramaAddressObject

This resource allows you to add/update/delete address objects on Panorama.

## Properties

`Name` - (Required) The address object's name.

`DeviceGroup` - (Optional) The device group to put the address object into (default: `shared`).

`Type` - (Optional) The type of address object.  This can be `ip-netmask` (default), `ip-range`, or `fqdn`.

`Value` - (Required) The address object's value.  This can take various forms depending on what type of address object this is, but can be something like `192.168.80.150` or `192.168.80.0/24`.

`Description` - (Optional) The address object's description.

`Tags` - (Optional) List of administrative tags.


## See Also

* [panos_panorama_address_object](https://www.terraform.io/docs/providers/panos/r/panorama_address_object.html) in the _Terraform Provider Documentation_