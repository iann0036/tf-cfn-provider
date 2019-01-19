# Terraform::Google::BillingAccountIamPolicy

Allows management of the entire IAM policy for an existing Google Cloud Platform Billing Account.

~> **Warning:** Billing accounts have a default user that can be **overwritten**
by use of this resource. The safest alternative is to use multiple `google_billing_account_iam_binding`
   resources. If you do use this resource, the best way to be sure that you are
   not making dangerous changes is to start by importing your existing policy,
   and examining the diff very closely.

~> **Note:** This resource __must not__ be used in conjunction with
   `google_billing_account_iam_member` or `google_billing_account_iam_binding`
   or they will fight over what your policy should be.

## Properties

TBC

## See Also

* [google_billing_account_iam_policy](https://www.terraform.io/docs/providers/google/r/billing_account_iam_policy.html) in the _Terraform Provider Documentation_