# Terraform::Google::LoggingProjectExclusion

Manages a project-level logging exclusion. For more information see
[the official documentation](https://cloud.google.com/logging/docs/) and
[Excluding Logs](https://cloud.google.com/logging/docs/exclusions).

Note that you must have the "Logs Configuration Writer" IAM role (`roles/logging.configWriter`)
granted to the credentials used with Terraform.

## Properties

`Filter` - (Required) The filter to apply when excluding logs. Only log entries that match the filter are excluded. See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced-filters) for information on how to write a filter.

`Name` - (Required) The name of the logging exclusion.

`Description` - (Optional) A human-readable description.

`Disabled` - (Optional) Whether this exclusion rule should be disabled or not. This defaults to false.

`Project` - (Optional) The project to create the exclusion in. If omitted, the project associated with the provider is used.


## See Also

* [google_logging_project_exclusion](https://www.terraform.io/docs/providers/google/r/logging_project_exclusion.html) in the _Terraform Provider Documentation_