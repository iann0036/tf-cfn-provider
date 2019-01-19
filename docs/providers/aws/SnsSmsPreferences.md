# Terraform::AWS::SnsSmsPreferences

Provides a way to set SNS SMS preferences.

## Properties

`MonthlySpendLimit` - (Optional) The maximum amount in USD that you are willing to spend each month to send SMS messages.

`DeliveryStatusIamRoleArn` - (Optional) The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs.

`DeliveryStatusSuccessSamplingRate` - (Optional) The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value must be between 0 and 100.

`DefaultSenderId` - (Optional) A string, such as your business brand, that is displayed as the sender on the receiving device.

`DefaultSmsType` - (Optional) The type of SMS message that you will send by default. Possible values are: Promotional, Transactional.

`UsageReportS3Bucket` - (Optional) The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS.


## See Also

* [aws_sns_sms_preferences](https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences.html) in the _Terraform Provider Documentation_