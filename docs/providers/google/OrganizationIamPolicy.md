# Terraform::Google::OrganizationIamPolicy

Allows management of the entire IAM policy for an existing Google Cloud Platform Organization.

~> **Warning:** New organizations have several default policies which will,
   without extreme caution, be **overwritten** by use of this resource.
   The safest alternative is to use multiple `google_organization_iam_binding`
   resources.  It is easy to use this resource to remove your own access to
   an organization, which will require a call to Google Support to have
   fixed, and can take multiple days to resolve.  If you do use this resource,
   the best way to be sure that you are not making dangerous changes is to start
   by importing your existing policy, and examining the diff very closely.

~> **Note:** This resource __must not__ be used in conjunction with
   `google_organization_iam_member` or `google_organization_iam_binding`
   or they will fight over what your policy should be.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [google_organization_iam_policy](https://www.terraform.io/docs/providers/google/r/organization_iam_policy.html) in the _Terraform Provider Documentation_