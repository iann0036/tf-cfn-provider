# Terraform::HuaweiCloud::IdentityRoleAssignmentV3

Manages a V3 Role assignment within group on HuaweiCloud IAM Service.

Note: You _must_ have admin privileges in your HuaweiCloud cloud to use
this resource.

## Properties

`DomainId` - (Optional; Required if `ProjectId` is empty) The domain to assign the role in.

`GroupId` - (Optional; Required if `user_id` is empty) The group to assign the role to.

`ProjectId` - (Optional; Required if `DomainId` is empty) The project to assign the role in.

`RoleId` - (Required) The role to assign.


## Return Values

### Fn::GetAtt

`DomainId` - See Properties above.

`ProjectId` - See Properties above.

`GroupId` - See Properties above.

`RoleId` - See Properties above.

## See Also

* [huaweicloud_identity_role_assignment_v3](https://www.terraform.io/docs/providers/huaweicloud/r/identity_role_assignment_v3.html) in the _Terraform Provider Documentation_