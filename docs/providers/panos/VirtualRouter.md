# Terraform::Panos::VirtualRouter

This resource allows you to add/update/delete virtual routers.

**Note** - The `default` virtual router may be configured with this resource,
however it will not be deleted from the firewall.  It will only be unexported
from the vsys that it is currently imported in, and any interfaces imported
into the virtual router will be removed.

This resource has some overlap with the `panos_virtual_router_entry`
resource.  If you want to use this resource with the other one, then make
sure that your `panos_virtual_router` spec does not define the
`interfaces` field.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [panos_virtual_router](https://www.terraform.io/docs/providers/panos/r/virtual_router.html) in the _Terraform Provider Documentation_