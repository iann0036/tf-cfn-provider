# Terraform::Google::OrganizationIamPolicy

Allows management of the entire IAM policy for an existing Google Cloud Platform Organization.

~> **Warning:** New organizations have several default policies which will,
   without extreme caution, be **overwritten** by use of this resource.
   The safest alternative is to use multiple `Terraform::Google::OrganizationIamBinding`
   resources.  It is easy to use this resource to remove your own access to
   an organization, which will require a call to Google Support to have
   fixed, and can take multiple days to resolve.  If you do use this resource,
   the best way to be sure that you are not making dangerous changes is to start
   by importing your existing policy, and examining the diff very closely.

~> **Note:** This resource __must not__ be used in conjunction with
   `Terraform::Google::OrganizationIamMember` or `googleOrganizationIamBinding`
   or they will fight over what your policy should be.

## Properties

`OrgId` - (Required) The numeric ID of the organization in which you want to create a custom role.

`PolicyData` - (Required) The `Terraform::Google::IamPolicy` data source that represents
the IAM policy that will be applied to the organization. This policy overrides any existing
policy applied to the organization.


## See Also

* [google_organization_iam_policy](https://www.terraform.io/docs/providers/google/r/organization_iam_policy.html) in the _Terraform Provider Documentation_