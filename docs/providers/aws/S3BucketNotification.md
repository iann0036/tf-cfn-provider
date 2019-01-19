# Terraform::AWS::S3BucketNotification

Provides a S3 bucket notification resource.

## Properties

`Bucket` - (Required) The name of the bucket to put notification configuration.

`Topic` - (Optional) The notification configuration to SNS Topic (documented below).

`Queue` - (Optional) The notification configuration to SQS Queue (documented below).

`LambdaFunction` - (Optional, Multiple) Used to configure notifications to a Lambda Function (documented below).

### Topic Properties

`Id` - (Optional) Specifies unique identifier for each of the notification configurations.

`TopicArn` - (Required) Specifies Amazon SNS topic ARN.

`Events` - (Required) Specifies [event](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html#notification-how-to-event-types-and-destinations) for which to send notifications.

`FilterPrefix` - (Optional) Specifies object key name prefix.

`FilterSuffix` - (Optional) Specifies object key name suffix.

### Queue Properties

`Id` - (Optional) Specifies unique identifier for each of the notification configurations.

`QueueArn` - (Required) Specifies Amazon SQS queue ARN.

`Events` - (Required) Specifies [event](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html#notification-how-to-event-types-and-destinations) for which to send notifications.

`FilterPrefix` - (Optional) Specifies object key name prefix.

`FilterSuffix` - (Optional) Specifies object key name suffix.

### LambdaFunction Properties

`Id` - (Optional) Specifies unique identifier for each of the notification configurations.

`LambdaFunctionArn` - (Required) Specifies Amazon Lambda function ARN.

`Events` - (Required) Specifies [event](http://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html#notification-how-to-event-types-and-destinations) for which to send notifications.

`FilterPrefix` - (Optional) Specifies object key name prefix.

`FilterSuffix` - (Optional) Specifies object key name suffix.


## See Also

* [aws_s3_bucket_notification](https://www.terraform.io/docs/providers/aws/r/s3_bucket_notification.html) in the _Terraform Provider Documentation_