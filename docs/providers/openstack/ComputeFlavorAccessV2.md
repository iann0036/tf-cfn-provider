# Terraform::OpenStack::ComputeFlavorAccessV2

Manages a project access for flavor V2 resource within OpenStack.

Note: You _must_ have admin privileges in your OpenStack cloud to use
this resource.

---

## Properties

`Region` - (Optional) The region in which to obtain the V2 Compute client.
If omitted, the `Region` argument of the provider is used.
Changing this creates a new flavor access.

`FlavorId` - (Required) The UUID of flavor to use. Changing this creates a new flavor access.

`TenantId` - (Required) The UUID of tenant which is allowed to use the flavor.
Changing this creates a new flavor access.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`FlavorId` - See Properties above.

`TenantId` - See Properties above.

## See Also

* [openstack_compute_flavor_access_v2](https://www.terraform.io/docs/providers/openstack/r/compute_flavor_access_v2.html) in the _Terraform Provider Documentation_