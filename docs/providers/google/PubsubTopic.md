# Terraform::Google::PubsubTopic

Creates a topic in Google's pubsub queueing system. For more information see
[the official documentation](https://cloud.google.com/pubsub/docs) and
[API](https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics).

## Properties

`Name` - (Required) A unique name for the pubsub topic. Changing this forces a new resource to be created.

`Project` - (Optional) The ID of the project in which the resource belongs. If it is not provided, the provider project is used.


## See Also

* [google_pubsub_topic](https://www.terraform.io/docs/providers/google/r/pubsub_topic.html) in the _Terraform Provider Documentation_