# Terraform::Google::PubsubSubscription

Creates a subscription in Google's pubsub queueing system. For more information see
[the official documentation](https://cloud.google.com/pubsub/docs) and
[API](https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions).

## Properties

`Name` - (Required) A unique name for the resource, required by pubsub. Changing this forces a new resource to be created.

`Topic` - (Required) The topic name or id to bind this subscription to, required by pubsub. Changing this forces a new resource to be created.

`AckDeadlineSeconds` - (Optional) The maximum number of seconds a subscriber has to acknowledge a received message, otherwise the message is redelivered. Changing this forces a new resource to be created.

`Project` - (Optional) The ID of the project in which the resource belongs. If it is not provided, the provider project is used.

`PushConfig` - (Optional) Block configuration for push options. More configuration options are detailed below.

### PushConfig Properties

`PushEndpoint` - (Required) The URL of the endpoint to which messages should be pushed. Changing this forces a new resource to be created.

`Attributes` - (Optional) Key-value pairs of API supported attributes used to control aspects of the message delivery. Currently, only `x-goog-version` is supported, which controls the format of the data delivery. For more information, read [the API docs here](https://cloud.google.com/pubsub/reference/rest/v1/projects.subscriptions#PushConfig.FIELDS.attributes). Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Path` - Path of the subscription in the format `projects/{project}/subscriptions/{sub}`.

## See Also

* [google_pubsub_subscription](https://www.terraform.io/docs/providers/google/r/pubsub_subscription.html) in the _Terraform Provider Documentation_