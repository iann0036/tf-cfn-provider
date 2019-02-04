# Terraform::Panos::PanoramaAddressGroup

This resource allows you to add/update/delete Panorama address groups.

Address groups are either statically defined or dynamically defined, so only
`StaticAddresses` or `DynamicMatch` should be defined within a given address
group.

## Properties

`Name` - (Required) The address group's name.

`DeviceGroup` - (Optional) The device group to put the address group into
(default: `shared`).

`StaticAddresses` - (Optional) The address objects to include in this
statically defined address group.

`DynamicMatch` - (Optional) The IP tags to include in this DAG.

`Description` - (Optional) The address group's description.

`Tags` - (Optional) List of administrative tags.


## See Also

* [panos_panorama_address_group](https://www.terraform.io/docs/providers/panos/r/panorama_address_group.html) in the _Terraform Provider Documentation_