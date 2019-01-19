# Terraform::AWS::PinpointSmsChannel

Provides a Pinpoint SMS Channel resource.

## Properties

`ApplicationId` - (Required) The application ID.

`Enabled` - (Optional) Whether the channel is enabled or disabled. Defaults to `true`.

`SenderId` - (Optional) Sender identifier of your messages.

`ShortCode` - (Optional) The Short Code registered with the phone provider.


## Return Values

### Fn::GetAtt

`PromotionalMessagesPerSecond` - Promotional messages per second that can be sent.

`TransactionalMessagesPerSecond` - Transactional messages per second that can be sent.

## See Also

* [aws_pinpoint_sms_channel](https://www.terraform.io/docs/providers/aws/r/pinpoint_sms_channel.html) in the _Terraform Provider Documentation_