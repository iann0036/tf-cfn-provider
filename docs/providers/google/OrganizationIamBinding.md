# Terraform::Google::OrganizationIamBinding

Allows creation and management of a single binding within IAM policy for
an existing Google Cloud Platform Organization.

~> **Note:** This resource __must not__ be used in conjunction with
   `google_organization_iam_member` for the __same role__ or they will fight over
   what your policy should be.

~> **Note:** On create, this resource will overwrite members of any existing roles.
    Use `terraform import` and inspect the `terraform plan` output to ensure
    your existing members are preserved.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Etag` - (Computed) The etag of the organization's IAM policy.

## See Also

* [google_organization_iam_binding](https://www.terraform.io/docs/providers/google/r/organization_iam_binding.html) in the _Terraform Provider Documentation_