# Terraform::Gitlab::Project

This resource allows you to create and manage projects within your
GitLab group or within your user.

## Properties

`Name` - (Required) The name of the project.

`Path` - (Optional) The path of the repository.

`NamespaceId` - (Optional) The namespace (group or user) of the project. Defaults to your user.
See [`Terraform::Gitlab::Group`](group.html) for an example.

`Description` - (Optional) A description of the project.

`DefaultBranch` - (Optional) The default branch for the project.

`IssuesEnabled` - (Optional) Enable issue tracking for the project.

`MergeRequestsEnabled` - (Optional) Enable merge requests for the project.

`WikiEnabled` - (Optional) Enable wiki for the project.

`SnippetsEnabled` - (Optional) Enable snippets for the project.

`VisibilityLevel` - (Optional) Set to `public` to create a public project.
Valid values are `private`, `internal`, `public`.
Repositories are created as private by default.

`SharedWithGroups` - (Optional) Enable sharing the project with a list of groups (maps).
* `GroupId` - (Required) Group id of the group you want to share the project with.
* `GroupAccessLevel` - (Optional) Group's sharing permissions. See [group members permission][group_members_permissions] for more info.
Valid values are `guest`, `reporter`, `developer`, `master`.

`GroupId` - (Required) Group id of the group you want to share the project with.
* `GroupAccessLevel` - (Optional) Group's sharing permissions. See [group members permission][group_members_permissions] for more info.
Valid values are `guest`, `reporter`, `developer`, `master`.

`GroupAccessLevel` - (Optional) Group's sharing permissions. See [group members permission][group_members_permissions] for more info.
Valid values are `guest`, `reporter`, `developer`, `master`.


## Return Values

### Fn::GetAtt

`Id` - Integer that uniquely identifies the project within the gitlab install.

`SshUrlToRepo` - URL that can be provided to `git clone` to clone the.

`HttpUrlToRepo` - URL that can be provided to `git clone` to clone the.

`WebUrl` - URL that can be used to find the project in a browser.

`RunnersToken` - Registration token to use during runner setup.

`SharedWithGroups` - List of the groups the project is shared with.

`GroupName` - Group's name.

## See Also

* [gitlab_project](https://www.terraform.io/docs/providers/gitlab/r/project.html) in the _Terraform Provider Documentation_