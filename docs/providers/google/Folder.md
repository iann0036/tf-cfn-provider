# Terraform::Google::Folder

Allows management of a Google Cloud Platform folder. For more information see 
[the official documentation](https://cloud.google.com/resource-manager/docs/creating-managing-folders)
and 
[API](https://cloud.google.com/resource-manager/reference/rest/v2/folders).

A folder can contain projects, other folders, or a combination of both. You can use folders to group projects under an organization in a hierarchy. For example, your organization might contain multiple departments, each with its own set of Cloud Platform resources. Folders allows you to group these resources on a per-department basis. Folders are used to group resources that share common IAM policies.

Folders created live inside an Organization. See the [Organization documentation](https://cloud.google.com/resource-manager/docs/quickstarts) for more details.

The service account used to run Terraform when creating a `google_folder`
resource must have `roles/resourcemanager.folderCreator`. See the
[Access Control for Folders Using IAM](https://cloud.google.com/resource-manager/docs/access-control-folders)
doc for more information.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Name` - The resource name of the Folder. Its format is folders/{folder_id}.

`LifecycleState` - The lifecycle state of the folder such as `ACTIVE` or `DELETE_REQUESTED`.

`CreateTime` - Timestamp when the Folder was created. Assigned by the server.

## See Also

* [google_folder](https://www.terraform.io/docs/providers/google/r/folder.html) in the _Terraform Provider Documentation_