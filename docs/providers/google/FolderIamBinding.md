# Terraform::Google::FolderIamBinding

Allows creation and management of a single binding within IAM policy for
an existing Google Cloud Platform folder.

~> **Note:** This resource _must not_ be used in conjunction with
   `Terraform::Google::FolderIamPolicy` or they will fight over what your policy
   should be.

~> **Note:** On create, this resource will overwrite members of any existing roles.
    Use `terraform import` and inspect the `terraform plan` output to ensure
    your existing members are preserved.

## Properties

`Folder` - (Required) The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.

`Role` - (Required) The role that should be applied. Only one `Terraform::Google::FolderIamBinding` can be used per role. Note that custom roles must be of the format `[projects|organizations]/{parent-name}/roles/{role-name}`.


## Return Values

### Fn::GetAtt

`Etag` - (Computed) The etag of the folder's IAM policy.

## See Also

* [google_folder_iam_binding](https://www.terraform.io/docs/providers/google/r/folder_iam_binding.html) in the _Terraform Provider Documentation_