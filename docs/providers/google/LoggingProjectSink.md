# Terraform::Google::LoggingProjectSink

Manages a project-level logging sink. For more information see
[the official documentation](https://cloud.google.com/logging/docs/),
[Exporting Logs in the API](https://cloud.google.com/logging/docs/api/tasks/exporting-logs)
and
[API](https://cloud.google.com/logging/docs/reference/v2/rest/).

~> **Note:** You must have [granted the "Logs Configuration Writer"](https://cloud.google.com/logging/docs/access-control) IAM role (`roles/logging.configWriter`) to the credentials used with terraform.

~> **Note** You must [enable the Cloud Resource Manager API](https://console.cloud.google.com/apis/library/cloudresourcemanager.googleapis.com)

## Properties

`Name` - (Required) The name of the logging sink.

`Destination` - (Required) The destination of the sink (or, in other words, where logs are written to). Can be a Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples: ``` "storage.googleapis.com/[GCS_BUCKET]" "bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]" "pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]" ``` The writer associated with the sink must have access to write to the above resource.

`Filter` - (Optional) The filter to apply when exporting logs. Only log entries that match the filter are exported. See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to write a filter.

`Project` - (Optional) The ID of the project to create the sink in. If omitted, the project associated with the provider is used.

`UniqueWriterIdentity` - (Optional) Whether or not to create a unique identity associated with this sink. If `false` (the default), then the `writer_identity` used is `serviceAccount:cloud-logs@system.gserviceaccount.com`. If `true`, then a unique service account is created and used for this sink. If you wish to publish logs across projects, you must set `UniqueWriterIdentity` to true.


## Return Values

### Fn::GetAtt

`WriterIdentity` - The identity associated with this sink. This identity must be granted write access to the.

## See Also

* [google_logging_project_sink](https://www.terraform.io/docs/providers/google/r/logging_project_sink.html) in the _Terraform Provider Documentation_