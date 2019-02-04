# Terraform::OpenTelekomCloud::SmnSubscriptionV2

Manages a V2 subscription resource within OpenTelekomCloud.

## Properties

`TopicUrn` - (Required) Resource identifier of a topic, which is unique.

`Endpoint` - (Required) Message endpoint.
For an HTTP subscription, the endpoint starts with http\://.
For an HTTPS subscription, the endpoint starts with https\://.
For an email subscription, the endpoint is a mail address.
For an SMS message subscription, the endpoint is a phone number.

`Protocol` - (Required) Protocol of the message endpoint. Currently, email,
sms, http, and https are supported.

`Remark` - (Optional) Remark information. The remarks must be a UTF-8-coded
character string containing 128 bytes.

`SubscriptionUrn` - (Optional) Resource identifier of a subscription, which
is unique.

`Owner` - (Optional) Project ID of the topic creator.

`Status` - (Optional) Subscription status.
0 indicates that the subscription is not confirmed.
1 indicates that the subscription is confirmed.
3 indicates that the subscription is canceled.


## Return Values

### Fn::GetAtt

`TopicUrn` - See Properties above.

`Endpoint` - See Properties above.

`Protocol` - See Properties above.

`Remark` - See Properties above.

`SubscriptionUrn` - See Properties above.

`Owner` - See Properties above.

`Status` - See Properties above.

## See Also

* [opentelekomcloud_smn_subscription_v2](https://www.terraform.io/docs/providers/opentelekomcloud/r/smn_subscription_v2.html) in the _Terraform Provider Documentation_