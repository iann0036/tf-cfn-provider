# Terraform::Google::PubsubSubscription

Creates a subscription in Google's pubsub queueing system. For more information see
[the official documentation](https://cloud.google.com/pubsub/docs) and
[API](https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Path` - Path of the subscription in the format `projects/{project}/subscriptions/{sub}`.

## See Also

* [google_pubsub_subscription](https://www.terraform.io/docs/providers/google/r/pubsub_subscription.html) in the _Terraform Provider Documentation_