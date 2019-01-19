# Terraform::Google::LoggingBillingAccountSink

Manages a billing account logging sink. For more information see
[the official documentation](https://cloud.google.com/logging/docs/) and
[Exporting Logs in the API](https://cloud.google.com/logging/docs/api/tasks/exporting-logs).

~> **Note** You must have the "Logs Configuration Writer" IAM role (`roles/logging.configWriter`)
[granted on the billing account](https://cloud.google.com/billing/reference/rest/v1/billingAccounts/getIamPolicy) to
the credentials used with Terraform. [IAM roles granted on a billing account](https://cloud.google.com/billing/docs/how-to/billing-access) are separate from the
typical IAM roles granted on a project.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`WriterIdentity` - The identity associated with this sink. This identity must be granted write access to the.

## See Also

* [google_logging_billing_account_sink](https://www.terraform.io/docs/providers/google/r/logging_billing_account_sink.html) in the _Terraform Provider Documentation_