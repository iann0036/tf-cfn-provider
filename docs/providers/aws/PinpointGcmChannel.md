# Terraform::AWS::PinpointGcmChannel

Provides a Pinpoint GCM Channel resource.

~> **Note:** Api Key argument will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Properties

`ApplicationId` - (Required) The application ID.

`ApiKey` - (Required) Platform credential API key from Google.

`Enabled` - (Optional) Whether the channel is enabled or disabled. Defaults to `true`.


## See Also

* [aws_pinpoint_gcm_channel](https://www.terraform.io/docs/providers/aws/r/pinpoint_gcm_channel.html) in the _Terraform Provider Documentation_