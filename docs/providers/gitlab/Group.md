# Terraform::Gitlab::Group

This resource allows you to create and manage GitLab groups.
Note your provider will need to be configured with admin-level access for this resource to work.

## Properties

`Name` - (Required) The name of this group.

`Path` - (Required) The path of the group.

`Description` - (Optional) The description of the group.

`LfsEnabled` - (Optional) Boolean, defaults to true.  Whether to enable LFS support for projects in this group.

`RequestAccessEnabled` - (Optional) Boolean, defaults to false.  Whether to enable users to request access to the group.

`VisibilityLevel` - (Optional) Set to `public` to create a public group. Valid values are `private`, `internal`, `public`. Groups are created as private by default.

`ParentId` - (Optional) Integer, id of the parent group (creates a nested group).


## Return Values

### Fn::GetAtt

`Id` - The unique id assigned to the group by the GitLab server.  Serves as a.

## See Also

* [gitlab_group](https://www.terraform.io/docs/providers/gitlab/r/group.html) in the _Terraform Provider Documentation_