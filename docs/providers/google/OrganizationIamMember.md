# Terraform::Google::OrganizationIamMember

Allows creation and management of a single member for a single binding within
the IAM policy for an existing Google Cloud Platform Organization.

~> **Note:** This resource __must not__ be used in conjunction with
   `google_organization_iam_binding` for the __same role__ or they will fight over
   what your policy should be.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Etag` - (Computed) The etag of the organization's IAM policy.

## See Also

* [google_organization_iam_member](https://www.terraform.io/docs/providers/google/r/organization_iam_member.html) in the _Terraform Provider Documentation_