# Terraform::AWS::KinesisAnalyticsApplication

Provides a Kinesis Analytics Application resource. Kinesis Analytics is a managed service that
allows processing and analyzing streaming data using standard SQL.

For more details, see the [Amazon Kinesis Analytics Documentation][1].

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ARN of the Kinesis Analytics Application.

`Arn` - The ARN of the Kinesis Analytics Appliation.

`CreateTimestamp` - The Timestamp when the application version was created.

`LastUpdateTimestamp` - The Timestamp when the application was last updated.

`Status` - The Status of the application.

`Version` - The Version of the application.

## See Also

* [aws_kinesis_analytics_application](https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application.html) in the _Terraform Provider Documentation_