# Terraform::AWS::AutoscalingNotification

Provides an AutoScaling Group with Notification support, via SNS Topics. Each of
the `notifications` map to a [Notification Configuration][2] inside Amazon Web
Services, and are applied to each AutoScaling Group you supply.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [aws_autoscaling_notification](https://www.terraform.io/docs/providers/aws/r/autoscaling_notification.html) in the _Terraform Provider Documentation_