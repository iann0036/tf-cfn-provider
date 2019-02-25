# Terraform::OpenTelekomCloud::IdentityRoleAssignmentV3

Manages a V3 Role assignment within group on OpentelekomCloud IAM Service.

Note: You _must_ have admin privileges in your OpentelekomCloud cloud to use
this resource.

## Properties

`DomainId` - (Optional; Required if `ProjectId` is empty) The domain to assign the role in.

`GroupId` - (Optional; Required if `UserId` is empty) The group to assign the role to.

`ProjectId` - (Optional; Required if `DomainId` is empty) The project to assign the role in.

`UserId` - (Optional; Required if `GroupId` is empty) The user to assign the role in.

`RoleId` - (Required) The role to assign.


## Return Values

### Fn::GetAtt

`DomainId` - See Properties above.

`ProjectId` - See Properties above.

`GroupId` - See Properties above.

`UserId` - See Properties above.

`RoleId` - See Properties above.

## See Also

* [opentelekomcloud_identity_role_assignment_v3](https://www.terraform.io/docs/providers/opentelekomcloud/r/identity_role_assignment_v3.html) in the _Terraform Provider Documentation_