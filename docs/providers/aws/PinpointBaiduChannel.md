# Terraform::AWS::PinpointBaiduChannel

Provides a Pinpoint Baidu Channel resource.

~> **Note:** All arguments including the Api Key and Secret Key will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Properties

`ApplicationId` - (Required) The application ID.

`Enabled` - (Optional) Specifies whether to enable the channel. Defaults to `true`.

`ApiKey` - (Required) Platform credential API key from Baidu.

`SecretKey` - (Required) Platform credential Secret key from Baidu.


## See Also

* [aws_pinpoint_baidu_channel](https://www.terraform.io/docs/providers/aws/r/pinpoint_baidu_channel.html) in the _Terraform Provider Documentation_