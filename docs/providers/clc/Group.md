# Terraform::CLC::Group

Manages a CLC server group. Either provisions or resolves to an existing group.

See also [Complete API documentation](https://www.ctl.io/api-docs/v2/#groups).

## Properties

`Name` - (Required, string) The name (or GUID) of this server group. Will resolve to existing if present.

`Parent` - (Required, string) The name or ID of the parent group. Will error if absent or unable to resolve.

`ParentGroupId` - (Computed) The ID of the parent group.

`LocationId` - (Required, string) The datacenter location of both parent group and this group. Examples: "WA1", "VA1".

`Description` - (Optional, string) Description for server group (visible in control portal only).

`CustomFields` - (Optional) See [CustomFields](#custom_fields) below for details.


## See Also

* [clc_group](https://www.terraform.io/docs/providers/clc/r/group.html) in the _Terraform Provider Documentation_