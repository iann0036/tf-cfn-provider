# Terraform::Google::CloudfunctionsFunction

Creates a new Cloud Function. For more information see
[the official documentation](https://cloud.google.com/functions/docs/)
and
[API](https://cloud.google.com/functions/docs/apis).

## Properties

`Name` - (Required) A user-defined name of the function. Function names must be unique globally.

`Description` - (Optional) Description of the function.

`AvailableMemoryMb` - (Optional) Memory (in MB), available to the function. Default value is 256MB. Allowed values are: 128MB, 256MB, 512MB, 1024MB, and 2048MB.

`Timeout` - (Optional) Timeout (in seconds) for the function. Default value is 60 seconds. Cannot be more than 540 seconds.

`EntryPoint` - (Optional) Name of the function that will be executed when the Google Cloud Function is triggered.

`EventTrigger` - (Optional) A source that fires events in response to a condition in another service. Structure is documented below. Cannot be used with `TriggerHttp`.

`TriggerHttp` - (Optional) Boolean variable. Any HTTP request (of a supported type) to the endpoint will trigger function execution. Supported HTTP request types are: POST, PUT, GET, DELETE, and OPTIONS. Endpoint is returned as `https_trigger_url`. Cannot be used with `trigger_bucket` and `trigger_topic`.

`Labels` - (Optional) A set of key/value label pairs to assign to the function.

`Runtime` - (Optional) The runtime in which the function is going to run. If empty, defaults to `"nodejs6"`.

`EnvironmentVariables` - (Optional) A set of key/value environment variable pairs to assign to the function.

`SourceArchiveBucket` - (Optional) The GCS bucket containing the zip archive which contains the function.

`SourceArchiveObject` - (Optional) The source archive object (file) in archive bucket.

`SourceRepository` - (Optional) Represents parameters related to source repository where a function is hosted. Cannot be set alongside `SourceArchiveBucket` or `SourceArchiveObject`. Structure is documented below.

`EventType` - (Required) The type of event to observe. For example: `"google.storage.object.finalize"`. See the documentation on [calling Cloud Functions](https://cloud.google.com/functions/docs/calling/) for a full reference. Cloud Storage, Cloud Pub/Sub and Cloud Firestore triggers are supported at this time. Legacy triggers are supported, such as `"providers/cloud.storage/eventTypes/object.change"`, `"providers/cloud.pubsub/eventTypes/topic.publish"` and `"providers/cloud.firestore/eventTypes/document.create"`.

`Resource` - (Required) Required. The name of the resource from which to observe events, for example, `"myBucket"`.

`FailurePolicy` - (Optional) Specifies policy for failed executions. Structure is documented below.

`Retry` - (Required) Whether the function should be retried on failure. Defaults to `false`.

`Url` - (Required) The URL pointing to the hosted repository where the function is defined. There are supported Cloud Source Repository URLs in the following formats:.


## Return Values

### Fn::GetAtt

`HttpsTriggerUrl` - URL which triggers function execution. Returned only if `TriggerHttp` is used.

`SourceReposoitory.0.deployedUrl` - The URL pointing to the hosted repository where the function was defined at the time of deployment.

`Project` - Project of the function. If it is not provided, the provider project is used.

`Region` - Region of function. Currently can be only "us-central1". If it is not provided, the provider region is used.

## See Also

* [google_cloudfunctions_function](https://www.terraform.io/docs/providers/google/r/cloudfunctions_function.html) in the _Terraform Provider Documentation_