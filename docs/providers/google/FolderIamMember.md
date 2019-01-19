# Terraform::Google::FolderIamMember

Allows creation and management of a single member for a single binding within
the IAM policy for an existing Google Cloud Platform folder.

~> **Note:** This resource _must not_ be used in conjunction with
   `google_folder_iam_policy` or they will fight over what your policy
   should be. Similarly, roles controlled by `google_folder_iam_binding`
   should not be assigned to using `google_folder_iam_member`.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Etag` - (Computed) The etag of the folder's IAM policy.

## See Also

* [google_folder_iam_member](https://www.terraform.io/docs/providers/google/r/folder_iam_member.html) in the _Terraform Provider Documentation_