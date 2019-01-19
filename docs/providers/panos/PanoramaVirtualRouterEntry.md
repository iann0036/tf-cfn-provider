# Terraform::Panos::PanoramaVirtualRouterEntry

This resource allows you to add/update/delete an interface in a Panorama
virtual router template.

This resource has some overlap with the `Terraform::Panos::PanoramaVirtualRouter`
resource.  If you want to use this resource with the other one, then make
sure that your `Terraform::Panos::PanoramaVirtualRouter` spec does not define the
`interfaces` field.

## Properties

`Template` - (Required) The template name.

`VirtualRouter` - (Required) The virtual router's name.

`Interface` - (Required) The interface to import into the virtual router.


## See Also

* [panos_panorama_virtual_router_entry](https://www.terraform.io/docs/providers/panos/r/panorama_virtual_router_entry.html) in the _Terraform Provider Documentation_