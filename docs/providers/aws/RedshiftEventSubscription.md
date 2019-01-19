# Terraform::AWS::RedshiftEventSubscription

Provides a Redshift event subscription resource.

## Properties

`Name` - (Required) The name of the Redshift event subscription.

`SnsTopicArn` - (Required) The ARN of the SNS topic to send events to.

`SourceIds` - (Optional) A list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. If specified, a source_type must also be specified.

`SourceType` - (Optional) The type of source that will be generating the events. Valid options are `cluster`, `cluster-parameter-group`, `cluster-security-group`, or `cluster-snapshot`. If not set, all sources will be subscribed to.

`Severity` - (Optional) The event severity to be published by the notification subscription. Valid options are `INFO` or `ERROR`.

`EventCategories` - (Optional) A list of event categories for a SourceType that you want to subscribe to. See https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-event-notifications.html or run `aws redshift describe-event-categories`.

`Enabled` - (Optional) A boolean flag to enable/disable the subscription. Defaults to true.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## See Also

* [aws_redshift_event_subscription](https://www.terraform.io/docs/providers/aws/r/redshift_event_subscription.html) in the _Terraform Provider Documentation_