# Terraform::HuaweiCloud::IdentityGroupMembershipV3

Manages a User Group Membership resource within HuaweiCloud IAM service.

Note: You _must_ have admin privileges in your HuaweiCloud cloud to use
this resource.

## Properties

`Group` - (Required) The group ID of this membership.

`Users` - (Required) A List of user IDs to associate to the group.


## Return Values

### Fn::GetAtt

`Group` - See Properties above.

`Users` - See Properties above.

## See Also

* [huaweicloud_identity_group_membership_v3](https://www.terraform.io/docs/providers/huaweicloud/r/identity_group_membership_v3.html) in the _Terraform Provider Documentation_