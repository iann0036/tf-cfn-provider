# Terraform::AWS::SesEventDestination

Provides an SES event destination

## Properties

`Name` - (Required) The name of the event destination.

`ConfigurationSetName` - (Required) The name of the configuration set.

`Enabled` - (Optional) If true, the event destination will be enabled.

`MatchingTypes` - (Required) A list of matching types. May be any of `"send"`, `"reject"`, `"bounce"`, `"complaint"`, `"delivery"`, `"open"`, `"click"`, or `"renderingFailure"`.

`CloudwatchDestination` - (Optional) CloudWatch destination for the events.

`KinesisDestination` - (Optional) Send the events to a kinesis firehose destination.

`SnsDestination` - (Optional) Send the events to an SNS Topic destination.


## See Also

* [aws_ses_event_destination](https://www.terraform.io/docs/providers/aws/r/ses_event_destination.html) in the _Terraform Provider Documentation_