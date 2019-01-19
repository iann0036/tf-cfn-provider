# Terraform::Google::FolderIamBinding

Allows creation and management of a single binding within IAM policy for
an existing Google Cloud Platform folder.

~> **Note:** This resource _must not_ be used in conjunction with
   `google_folder_iam_policy` or they will fight over what your policy
   should be.

~> **Note:** On create, this resource will overwrite members of any existing roles.
    Use `terraform import` and inspect the `terraform plan` output to ensure
    your existing members are preserved.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Etag` - (Computed) The etag of the folder's IAM policy.

## See Also

* [google_folder_iam_binding](https://www.terraform.io/docs/providers/google/r/folder_iam_binding.html) in the _Terraform Provider Documentation_