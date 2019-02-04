# Terraform::AWS::AutoscalingNotification

Provides an AutoScaling Group with Notification support, via SNS Topics. Each of
the `Notifications` map to a [Notification Configuration][2] inside Amazon Web
Services, and are applied to each AutoScaling Group you supply.

## Properties

`GroupNames` - (Required) A list of AutoScaling Group Names.

`Notifications` - (Required) A list of Notification Types that trigger
notifications. Acceptable values are documented [in the AWS documentation here][1].

`TopicArn` - (Required) The Topic ARN for notifications to be sent through.


## See Also

* [aws_autoscaling_notification](https://www.terraform.io/docs/providers/aws/r/autoscaling_notification.html) in the _Terraform Provider Documentation_