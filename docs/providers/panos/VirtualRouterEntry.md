# Terraform::Panos::VirtualRouterEntry

This resource allows you to add/update/delete an interface in a
virtual router.

This resource has some overlap with the `panos_virtual_router`
resource.  If you want to use this resource with the other one, then make
sure that your `panos_virtual_router` spec does not define the
`interfaces` field.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [panos_virtual_router_entry](https://www.terraform.io/docs/providers/panos/r/virtual_router_entry.html) in the _Terraform Provider Documentation_