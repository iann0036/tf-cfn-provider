# Terraform::Gitlab::GroupMembership

This resource allows you to add a user to an existing group.

## Properties

`GroupId` - (Required) The id of the group.

`UserId` - (Required) The id of the user.

`AccessLevel` - (Required)  Acceptable values are: guest, reporter, developer, master.

`ExpiresAt` - (Optional) Expiration date for the group membership. Format: `YYYY-MM-DD`.


## See Also

* [gitlab_group_membership](https://www.terraform.io/docs/providers/gitlab/r/group_membership.html) in the _Terraform Provider Documentation_