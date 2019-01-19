# Terraform::Google::LoggingOrganizationExclusion

Manages an organization-level logging exclusion. For more information see
[the official documentation](https://cloud.google.com/logging/docs/) and
[Excluding Logs](https://cloud.google.com/logging/docs/exclusions).

Note that you must have the "Logs Configuration Writer" IAM role (`roles/logging.configWriter`)
granted to the credentials used with Terraform.

## Properties

`Name` - (Required) The name of the logging exclusion.

`OrgId` - (Required) The organization to create the exclusion in.

`Description` - (Optional) A human-readable description.

`Disabled` - (Optional) Whether this exclusion rule should be disabled or not. This defaults to false.

`Filter` - (Required) The filter to apply when excluding logs. Only log entries that match the filter are excluded. See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced-filters) for information on how to write a filter.


## See Also

* [google_logging_organization_exclusion](https://www.terraform.io/docs/providers/google/r/logging_organization_exclusion.html) in the _Terraform Provider Documentation_