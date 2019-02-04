# Terraform::Google::LoggingBillingAccountExclusion

Manages a billing account logging exclusion. For more information see
[the official documentation](https://cloud.google.com/logging/docs/) and
[Excluding Logs](https://cloud.google.com/logging/docs/exclusions).

Note that you must have the "Logs Configuration Writer" IAM role (`roles/logging.configWriter`)
granted to the credentials used with Terraform.

## Properties

`BillingAccount` - (Required) The billing account to create the exclusion for.

`Name` - (Required) The name of the logging exclusion.

`Description` - (Optional) A human-readable description.

`Disabled` - (Optional) Whether this exclusion rule should be disabled or not. This defaults to
false.

`Filter` - (Required) The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced-filters) for information on how to
write a filter.


## See Also

* [google_logging_billing_account_exclusion](https://www.terraform.io/docs/providers/google/r/logging_billing_account_exclusion.html) in the _Terraform Provider Documentation_