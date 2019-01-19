# Terraform::Google::StorageNotification

Creates a new notification configuration on a specified bucket, establishing a flow of event notifications from GCS to a Cloud Pub/Sub topic.
 For more information see 
[the official documentation](https://cloud.google.com/storage/docs/pubsub-notifications) 
and 
[API](https://cloud.google.com/storage/docs/json_api/v1/notifications).

In order to enable notifications, a special Google Cloud Storage service account unique to the project
must have the IAM permission "projects.topics.publish" for a Cloud Pub/Sub topic in the project. To get the service
account's email address, use the `google_storage_project_service_account` datasource's `email_address` value, and see below
for an example of enabling notifications by granting the correct IAM permission. See
[the notifications documentation](https://cloud.google.com/storage/docs/gsutil/commands/notification) for more details.

## Properties

TBC

## Return Values

### Fn::GetAtt

`SelfLink` - The URI of the created resource.

## See Also

* [google_storage_notification](https://www.terraform.io/docs/providers/google/r/storage_notification.html) in the _Terraform Provider Documentation_