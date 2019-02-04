# Terraform::Google::BillingAccountIamPolicy

Allows management of the entire IAM policy for an existing Google Cloud Platform Billing Account.

~> **Warning:** Billing accounts have a default user that can be **overwritten**
by use of this resource. The safest alternative is to use multiple `Terraform::Google::BillingAccountIamBinding`
   resources. If you do use this resource, the best way to be sure that you are
   not making dangerous changes is to start by importing your existing policy,
   and examining the diff very closely.

~> **Note:** This resource __must not__ be used in conjunction with
   `Terraform::Google::BillingAccountIamMember` or `googleBillingAccountIamBinding`
   or they will fight over what your policy should be.

## Properties

`BillingAccountId` - (Required) The billing account id.

`PolicyData` - (Required) The `Terraform::Google::IamPolicy` data source that represents
the IAM policy that will be applied to the billing account. This policy overrides any existing
policy applied to the billing account.


## See Also

* [google_billing_account_iam_policy](https://www.terraform.io/docs/providers/google/r/billing_account_iam_policy.html) in the _Terraform Provider Documentation_