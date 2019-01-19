# Terraform::OCI::IdentityUserGroupMembership

This resource provides the User Group Membership resource in Oracle Cloud Infrastructure Identity service.

Adds the specified user to the specified group and returns a `UserGroupMembership` object with its own OCID.

## Properties

TBC

## Return Values

### Fn::GetAtt

`CompartmentId` - The OCID of the tenancy containing the user, group, and membership object.

`GroupId` - The OCID of the group.

`Id` - The OCID of the membership.

`InactiveState` - The detailed status of INACTIVE lifecycleState.

`State` - The membership's current state.

`TimeCreated` - Date and time the membership was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

`UserId` - The OCID of the user.

## See Also

* [oci_identity_user_group_membership](https://www.terraform.io/docs/providers/oci/r/identity_user_group_membership.html) in the _Terraform Provider Documentation_