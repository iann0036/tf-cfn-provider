# Terraform::AWS::CloudwatchLogSubscriptionFilter

Provides a CloudWatch Logs subscription filter resource.

## Properties

`Name` - (Required) A name for the subscription filter.

`DestinationArn` - (Required) The ARN of the destination to deliver matching log events to. Kinesis stream or Lambda function ARN.

`FilterPattern` - (Required) A valid CloudWatch Logs filter pattern for subscribing to a filtered stream of log events.

`LogGroupName` - (Required) The name of the log group to associate the subscription filter with.

`RoleArn` - (Optional) The ARN of an IAM role that grants Amazon CloudWatch Logs permissions to deliver ingested log events to the destination. If you use Lambda as a destination, you should skip this argument and use `Terraform::AWS::LambdaPermission` resource for granting access from CloudWatch logs to the destination Lambda function.

`Distribution` - (Optional) The method used to distribute log data to the destination. By default log data is grouped by log stream, but the grouping can be set to random for a more even distribution. This property is only applicable when the destination is an Amazon Kinesis stream. Valid values are "Random" and "ByLogStream".


## See Also

* [aws_cloudwatch_log_subscription_filter](https://www.terraform.io/docs/providers/aws/r/cloudwatch_log_subscription_filter.html) in the _Terraform Provider Documentation_