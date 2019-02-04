# Terraform::OpenStack::IdentityProjectV3

Manages a V3 Project resource within OpenStack Keystone.

Note: You _must_ have admin privileges in your OpenStack cloud to use
this resource.

## Properties

`Description` - (Optional) A description of the project.

`DomainId` - (Optional) The domain this project belongs to.

`Enabled` - (Optional) Whether the project is enabled or disabled. Valid
values are `true` and `false`.

`IsDomain` - (Optional) Whether this project is a domain. Valid values
are `true` and `false`.

`Name` - (Optional) The name of the project.

`ParentId` - (Optional) The parent of this project.

`Region` - (Optional) The region in which to obtain the V3 Keystone client.
If omitted, the `Region` argument of the provider is used. Changing this
creates a new User.


## Return Values

### Fn::GetAtt

`DomainId` - See Properties above.

`ParentId` - See Properties above.

## See Also

* [openstack_identity_project_v3](https://www.terraform.io/docs/providers/openstack/r/identity_project_v3.html) in the _Terraform Provider Documentation_