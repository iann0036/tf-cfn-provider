# Terraform::Google::LoggingOrganizationSink

Manages a organization-level logging sink. For more information see
[the official documentation](https://cloud.google.com/logging/docs/) and
[Exporting Logs in the API](https://cloud.google.com/logging/docs/api/tasks/exporting-logs).

Note that you must have the "Logs Configuration Writer" IAM role (`roles/logging.configWriter`)
granted to the credentials used with terraform.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`WriterIdentity` - The identity associated with this sink. This identity must be granted write access to the.

## See Also

* [google_logging_organization_sink](https://www.terraform.io/docs/providers/google/r/logging_organization_sink.html) in the _Terraform Provider Documentation_