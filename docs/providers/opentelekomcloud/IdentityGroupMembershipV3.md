# Terraform::OpenTelekomCloud::IdentityGroupMembershipV3

Manages a User Group Membership resource within OpentelekomCloud IAM service.

Note: You _must_ have admin privileges in your OpentelekomCloud cloud to use
this resource.

## Properties

`Group` - (Required) The group ID of this membership.

`Users` - (Required) A List of user IDs to associate to the group.


## Return Values

### Fn::GetAtt

`Group` - See Properties above.

`Users` - See Properties above.

## See Also

* [opentelekomcloud_identity_group_membership_v3](https://www.terraform.io/docs/providers/opentelekomcloud/r/identity_group_membership_v3.html) in the _Terraform Provider Documentation_