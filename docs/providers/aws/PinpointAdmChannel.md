# Terraform::AWS::PinpointAdmChannel

Provides a Pinpoint ADM (Amazon Device Messaging) Channel resource.

~> **Note:** All arguments including the Client ID and Client Secret will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Properties

`ApplicationId` - (Required) The application ID.

`ClientId` - (Required) Client ID (part of OAuth Credentials) obtained via Amazon Developer Account.

`ClientSecret` - (Required) Client Secret (part of OAuth Credentials) obtained via Amazon Developer Account.

`Enabled` - (Optional) Specifies whether to enable the channel. Defaults to `true`.


## See Also

* [aws_pinpoint_adm_channel](https://www.terraform.io/docs/providers/aws/r/pinpoint_adm_channel.html) in the _Terraform Provider Documentation_