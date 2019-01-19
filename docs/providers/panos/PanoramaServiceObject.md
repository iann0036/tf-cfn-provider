# Terraform::Panos::PanoramaServiceObject

This resource allows you to add/update/delete Panorama service objects.

## Properties

`Name` - (Required) The service object's name.

`DeviceGroup` - (Optional) The device group to put the service object into (default: `shared`).

`Description` - (Optional) The service object's description.

`Protocol` - (Required) The service's protocol.  This should be `tcp` or `udp`.

`SourcePort` - (Optional) The source port.  This can be a single port number, range (1-65535), or comma separated (80,8080,443).

`DestinationPort` - (Required) The destination port.  This can be a single port number, range (1-65535), or comma separated (80,8080,443).

`Tags` - (Optional) List of administrative tags.


## See Also

* [panos_panorama_service_object](https://www.terraform.io/docs/providers/panos/r/panorama_service_object.html) in the _Terraform Provider Documentation_