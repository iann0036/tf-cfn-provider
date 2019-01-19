# Terraform::AWS::PinpointEmailChannel

Provides a Pinpoint SMS Channel resource.

## Properties

`ApplicationId` - (Required) The application ID.

`Enabled` - (Optional) Whether the channel is enabled or disabled. Defaults to `true`.

`FromAddress` - (Required) The email address used to send emails from.

`Identity` - (Required) The ARN of an identity verified with SES.

`RoleArn` - (Required) The ARN of an IAM Role used to submit events to Mobile Analytics' event ingestion service.


## Return Values

### Fn::GetAtt

`MessagesPerSecond` - Messages per second that can be sent.

## See Also

* [aws_pinpoint_email_channel](https://www.terraform.io/docs/providers/aws/r/pinpoint_email_channel.html) in the _Terraform Provider Documentation_