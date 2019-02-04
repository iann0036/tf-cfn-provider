# Terraform::OpenTelekomCloud::IdentityRoleV3

Manages a V3 Role resource within OpentelekomCloud Keystone.

Note: You _must_ have admin privileges in your OpentelekomCloud cloud to use
this resource.

## Properties

`Name` - The name of the role.

`DomainId` - (Optional) The domain the role belongs to.

`Region` - (Optional) The region in which to obtain the IAM client.
If omitted, the `Region` argument of the provider is used. Changing this
creates a new Role.


## Return Values

### Fn::GetAtt

`Name` - See Properties above.

`DomainId` - See Properties above.

`Region` - See Properties above.

## See Also

* [opentelekomcloud_identity_role_v3](https://www.terraform.io/docs/providers/opentelekomcloud/r/identity_role_v3.html) in the _Terraform Provider Documentation_