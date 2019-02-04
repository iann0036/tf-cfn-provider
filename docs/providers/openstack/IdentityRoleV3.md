# Terraform::OpenStack::IdentityRoleV3

Manages a V3 Role resource within OpenStack Keystone.

Note: You _must_ have admin privileges in your OpenStack cloud to use
this resource.

## Properties

`Name` - The name of the role.

`DomainId` - (Optional) The domain the role belongs to.

`Region` - (Optional) The region in which to obtain the V3 Keystone client.
If omitted, the `Region` argument of the provider is used. Changing this
creates a new Role.


## Return Values

### Fn::GetAtt

`Name` - See Properties above.

`DomainId` - See Properties above.

`Region` - See Properties above.

## See Also

* [openstack_identity_role_v3](https://www.terraform.io/docs/providers/openstack/r/identity_role_v3.html) in the _Terraform Provider Documentation_