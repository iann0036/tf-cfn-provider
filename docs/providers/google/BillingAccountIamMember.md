# Terraform::Google::BillingAccountIamMember

Allows creation and management of a single member for a single binding within
the IAM policy for an existing Google Cloud Platform Billing Account.

~> **Note:** This resource __must not__ be used in conjunction with
   `Terraform::Google::BillingAccountIamBinding` for the __same role__ or they will fight over
   what your policy should be.

## Properties

`BillingAccountId` - (Required) The billing account id.

`Role` - (Required) The role that should be applied.

`Member` - (Required) The user that the role should apply to. For more details on format and restrictions see https://cloud.google.com/billing/reference/rest/v1/Policy#Binding.


## Return Values

### Fn::GetAtt

`Etag` - (Computed) The etag of the billing account's IAM policy.

## See Also

* [google_billing_account_iam_member](https://www.terraform.io/docs/providers/google/r/billing_account_iam_member.html) in the _Terraform Provider Documentation_