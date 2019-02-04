# Terraform::Google::StorageNotification

Creates a new notification configuration on a specified bucket, establishing a flow of event notifications from GCS to a Cloud Pub/Sub topic.
 For more information see 
[the official documentation](https://cloud.google.com/storage/docs/pubsub-notifications) 
and 
[API](https://cloud.google.com/storage/docs/json_api/v1/notifications).

In order to enable notifications, a special Google Cloud Storage service account unique to the project
must have the IAM permission "projects.topics.publish" for a Cloud Pub/Sub topic in the project. To get the service
account's email address, use the `Terraform::Google::StorageProjectServiceAccount` datasource's `emailAddress` value, and see below
for an example of enabling notifications by granting the correct IAM permission. See
[the notifications documentation](https://cloud.google.com/storage/docs/gsutil/commands/notification) for more details.

## Properties

`Bucket` - (Required) The name of the bucket.

`PayloadFormat` - (Required) The desired content of the Payload. One of `"JSON_API_V1"` or `"NONE"`.

`Topic` - (Required) The Cloud PubSub topic to which this subscription publishes. Expects either the
topic name, assumed to belong to the default GCP provider project, or the project-level name,
i.e. `projects/my-gcp-project/topics/my-topic` or `my-topic`.

`CustomAttributes` - (Optional)  A set of key/value attribute pairs to attach to each Cloud PubSub message published for this notification subscription.

`EventTypes` - (Optional) List of event type filters for this notification config. If not specified, Cloud Storage will send notifications for all event types. The valid types are: `"OBJECT_FINALIZE"`, `"OBJECT_METADATA_UPDATE"`, `"OBJECT_DELETE"`, `"OBJECT_ARCHIVE"`.

`ObjectNamePrefix` - (Optional) Specifies a prefix path filter for this notification config. Cloud Storage will only send notifications for objects in this bucket whose names begin with the specified prefix.


## Return Values

### Fn::GetAtt

`SelfLink` - The URI of the created resource.

## See Also

* [google_storage_notification](https://www.terraform.io/docs/providers/google/r/storage_notification.html) in the _Terraform Provider Documentation_