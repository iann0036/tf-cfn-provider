# Terraform::Google::FolderIamPolicy

Allows creation and management of the IAM policy for an existing Google Cloud
Platform folder.

## Properties

`Folder` - (Required) The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.

`PolicyData` - (Required) The `Terraform::Google::IamPolicy` data source that represents the IAM policy that will be applied to the folder. This policy overrides any existing policy applied to the folder.


## Return Values

### Fn::GetAtt

`Etag` - (Computed) The etag of the folder's IAM policy. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.

## See Also

* [google_folder_iam_policy](https://www.terraform.io/docs/providers/google/r/folder_iam_policy.html) in the _Terraform Provider Documentation_