# Terraform::Google::FolderIamMember

Allows creation and management of a single member for a single binding within
the IAM policy for an existing Google Cloud Platform folder.

~> **Note:** This resource _must not_ be used in conjunction with
   `Terraform::Google::FolderIamPolicy` or they will fight over what your policy
   should be. Similarly, roles controlled by `Terraform::Google::FolderIamBinding`
   should not be assigned to using `Terraform::Google::FolderIamMember`.

## Properties

`Folder` - (Required) The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.

`Member` - (Required) The identity that will be granted the privilege in the `Role`. For more details on format and restrictions see https://cloud.google.com/billing/reference/rest/v1/Policy#Binding
This field can have one of the following values:
* **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
* **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
* **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
* **domain:{domain}**: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.

`Role` - (Required) The role that should be applied. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.


## Return Values

### Fn::GetAtt

`Etag` - (Computed) The etag of the folder's IAM policy.

## See Also

* [google_folder_iam_member](https://www.terraform.io/docs/providers/google/r/folder_iam_member.html) in the _Terraform Provider Documentation_