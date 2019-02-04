# Terraform::Google::LoggingOrganizationSink

Manages a organization-level logging sink. For more information see
[the official documentation](https://cloud.google.com/logging/docs/) and
[Exporting Logs in the API](https://cloud.google.com/logging/docs/api/tasks/exporting-logs).

Note that you must have the "Logs Configuration Writer" IAM role (`roles/logging.configWriter`)
granted to the credentials used with terraform.

## Properties

`Name` - (Required) The name of the logging sink.

`OrgId` - (Required) The numeric ID of the organization to be exported to the sink.

`Destination` - (Required) The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
```
"storage.googleapis.com/[GCS_BUCKET]"
"bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]"
"pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]"
```
The writer associated with the sink must have access to write to the above resource.

`Filter` - (Optional) The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.

`IncludeChildren` - (Optional) Whether or not to include children organizations in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided organization are included.


## Return Values

### Fn::GetAtt

`WriterIdentity` - The identity associated with this sink. This identity must be granted write access to the.

## See Also

* [google_logging_organization_sink](https://www.terraform.io/docs/providers/google/r/logging_organization_sink.html) in the _Terraform Provider Documentation_