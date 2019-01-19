# Terraform::AWS::PinpointEventStream

Provides a Pinpoint Event Stream resource.

## Properties

`ApplicationId` - (Required) The application ID.

`DestinationStreamArn` - (Required) The Amazon Resource Name (ARN) of the Amazon Kinesis stream or Firehose delivery stream to which you want to publish events.

`RoleArn` - (Required) The IAM role that authorizes Amazon Pinpoint to publish events to the stream in your account.


## See Also

* [aws_pinpoint_event_stream](https://www.terraform.io/docs/providers/aws/r/pinpoint_event_stream.html) in the _Terraform Provider Documentation_