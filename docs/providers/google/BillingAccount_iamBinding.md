# Terraform::Google::BillingAccount_iamBinding

Allows creation and management of a single binding within IAM policy for
an existing Google Cloud Platform Billing Account.

~> **Note:** This resource __must not__ be used in conjunction with
   `google_billing_account_iam_member` for the __same role__ or they will fight over
   what your policy should be.

~> **Note:** On create, this resource will overwrite members of any existing roles.
    Use `terraform import` and inspect the `terraform plan` output to ensure
    your existing members are preserved.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Etag` - (Computed) The etag of the billing account's IAM policy.

## See Also

* [google_billing_account__iam_binding](https://www.terraform.io/docs/providers/google/r/billing_account__iam_binding.html) in the _Terraform Provider Documentation_