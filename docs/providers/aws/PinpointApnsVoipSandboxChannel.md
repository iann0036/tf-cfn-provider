# Terraform::AWS::PinpointApnsVoipSandboxChannel

Provides a Pinpoint APNs VoIP Sandbox Channel resource.

~> **Note:** All arguments, including certificates and tokens, will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Properties

`ApplicationId` - (Required) The application ID.

`Enabled` - (Optional) Whether the channel is enabled or disabled. Defaults to `true`.

`DefaultAuthenticationMethod` - (Optional) The default authentication method used for APNs.
__NOTE__: Amazon Pinpoint uses this default for every APNs push notification that you send using the console.
You can override the default when you send a message programmatically using the Amazon Pinpoint API, the AWS CLI, or an AWS SDK.
If your default authentication type fails, Amazon Pinpoint doesn't attempt to use the other authentication type.

`Certificate` - (Required) The pem encoded TLS Certificate from Apple.

`PrivateKey` - (Required) The Certificate Private Key file (ie. `.key` file).

`BundleId` - (Required) The ID assigned to your iOS app. To find this value, choose Certificates, IDs & Profiles, choose App IDs in the Identifiers section, and choose your app.

`TeamId` - (Required) The ID assigned to your Apple developer account team. This value is provided on the Membership page.

`TokenKey` - (Required) The `.p8` file that you download from your Apple developer account when you create an authentication key.

`TokenKeyId` - (Required) The ID assigned to your signing key. To find this value, choose Certificates, IDs & Profiles, and choose your key in the Keys section.


## See Also

* [aws_pinpoint_apns_voip_sandbox_channel](https://www.terraform.io/docs/providers/aws/r/pinpoint_apns_voip_sandbox_channel.html) in the _Terraform Provider Documentation_