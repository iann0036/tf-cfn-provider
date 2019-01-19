# Terraform::Alicloud::RamGroupMembership

Provides a RAM Group membership resource.

## Properties

`GroupName` - (Required, Forces new resource) Name of the RAM group. This name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphen "-", and must not begin with a hyphen.

`UserNames` - (Required) Set of user name which will be added to group. Each name can have a string of 1 to 64 characters, must contain only alphanumeric characters or hyphens, such as "-",".","_", and must not begin with a hyphen.


## Return Values

### Fn::GetAtt

`Id` - The membership ID.

`GroupName` - The group name.

`UserNames` - The list of names of users which in the group.

## See Also

* [alicloud_ram_group_membership](https://www.terraform.io/docs/providers/alicloud/r/ram_group_membership.html) in the _Terraform Provider Documentation_