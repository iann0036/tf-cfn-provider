# Terraform::Google::Folder

Allows management of a Google Cloud Platform folder. For more information see 
[the official documentation](https://cloud.google.com/resource-manager/docs/creating-managing-folders)
and 
[API](https://cloud.google.com/resource-manager/reference/rest/v2/folders).

A folder can contain projects, other folders, or a combination of both. You can use folders to group projects under an organization in a hierarchy. For example, your organization might contain multiple departments, each with its own set of Cloud Platform resources. Folders allows you to group these resources on a per-department basis. Folders are used to group resources that share common IAM policies.

Folders created live inside an Organization. See the [Organization documentation](https://cloud.google.com/resource-manager/docs/quickstarts) for more details.

The service account used to run Terraform when creating a `Terraform::Google::Folder`
resource must have `roles/resourcemanager.folderCreator`. See the
[Access Control for Folders Using IAM](https://cloud.google.com/resource-manager/docs/access-control-folders)
doc for more information.

## Properties

`DisplayName` - (Required) The folder’s display name.
A folder’s display name must be unique amongst its siblings, e.g. no two folders with the same parent can share the same display name. The display name must start and end with a letter or digit, may contain letters, digits, spaces, hyphens and underscores and can be no longer than 30 characters.

`Parent` - (Required) The resource name of the parent Folder or Organization.
Must be of the form `folders/{folder_id}` or `organizations/{org_id}`.


## Return Values

### Fn::GetAtt

`Name` - The resource name of the Folder. Its format is folders/{folder_id}.

`LifecycleState` - The lifecycle state of the folder such as `ACTIVE` or `DELETE_REQUESTED`.

`CreateTime` - Timestamp when the Folder was created. Assigned by the server.

## See Also

* [google_folder](https://www.terraform.io/docs/providers/google/r/folder.html) in the _Terraform Provider Documentation_