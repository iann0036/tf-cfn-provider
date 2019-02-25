# Terraform::AWS::KinesisAnalyticsApplication

Provides a Kinesis Analytics Application resource. Kinesis Analytics is a managed service that
allows processing and analyzing streaming data using standard SQL.

For more details, see the [Amazon Kinesis Analytics Documentation][1].

## Properties

`Name` - (Required) Name of the Kinesis Analytics Application.

`Code` - (Optional) SQL Code to transform input data, and generate output.

`Description` - (Optional) Description of the application.

`CloudwatchLoggingOptions` - (Optional) The CloudWatch log stream options to monitor application errors.
See [CloudWatch Logging Options](#cloudwatch-logging-options) below for more details.

`Inputs` - (Optional) Input configuration of the application. See [Inputs](#inputs) below for more details.

`Outputs` - (Optional) Output destination configuration of the application. See [Outputs](#outputs) below for more details.

`ReferenceDataSources` - (Optional) An S3 Reference Data Source for the application.
See [Reference Data Sources](#reference-data-sources) below for more details.


## Return Values

### Fn::GetAtt

`Status` - The Status of the application.

`LastUpdateTimestamp` - The Timestamp when the application was last updated.

`Version` - The Version of the application.

`CreateTimestamp` - The Timestamp when the application version was created.

`Id` - The ARN of the Kinesis Analytics Application.

`Arn` - The ARN of the Kinesis Analytics Appliation.

## See Also

* [aws_kinesis_analytics_application](https://www.terraform.io/docs/providers/aws/r/kinesis_analytics_application.html) in the _Terraform Provider Documentation_