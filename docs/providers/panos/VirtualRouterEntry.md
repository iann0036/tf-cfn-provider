# Terraform::Panos::VirtualRouterEntry

This resource allows you to add/update/delete an interface in a
virtual router.

This resource has some overlap with the `Terraform::Panos::VirtualRouter`
resource.  If you want to use this resource with the other one, then make
sure that your `Terraform::Panos::VirtualRouter` spec does not define the
`interfaces` field.

## Properties

`VirtualRouter` - (Required) The virtual router's name.

`Interface` - (Required) The interface to import into the virtual router.


## See Also

* [panos_virtual_router_entry](https://www.terraform.io/docs/providers/panos/r/virtual_router_entry.html) in the _Terraform Provider Documentation_