# Terraform::Panos::PanoramaVirtualRouter

This resource allows you to add/update/delete Panorama virtual routers
for templates.

**Note** - The `default` virtual router may be configured with this resource,
however it will not be deleted from Panorama.  It will only be unexported
from the vsys that it is currently imported in, and any interfaces imported
into the virtual router will be removed.

This resource has some overlap with the `panos_panorama_virtual_router_entry`
resource.  If you want to use this resource with the other one, then make
sure that your `panos_panorama_virtual_router` spec does not define the
`interfaces` field.

## Properties

TBC

## See Also

* [panos_panorama_virtual_router](https://www.terraform.io/docs/providers/panos/r/panorama_virtual_router.html) in the _Terraform Provider Documentation_