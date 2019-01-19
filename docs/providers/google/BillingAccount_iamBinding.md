# Terraform::Google::BillingAccount_iamBinding

Allows creation and management of a single binding within IAM policy for
an existing Google Cloud Platform Billing Account.

~> **Note:** This resource __must not__ be used in conjunction with
   `Terraform::Google::BillingAccountIamMember` for the __same role__ or they will fight over
   what your policy should be.

~> **Note:** On create, this resource will overwrite members of any existing roles.
    Use `terraform import` and inspect the `terraform plan` output to ensure
    your existing members are preserved.

## Properties

`BillingAccountId` - (Required) The billing account id.

`Role` - (Required) The role that should be applied.

`Members` - (Required) A list of users that the role should apply to. For more details on format and restrictions see https://cloud.google.com/billing/reference/rest/v1/Policy#Binding.


## Return Values

### Fn::GetAtt

`Etag` - (Computed) The etag of the billing account's IAM policy.

## See Also

* [google_billing_account__iam_binding](https://www.terraform.io/docs/providers/google/r/billing_account__iam_binding.html) in the _Terraform Provider Documentation_