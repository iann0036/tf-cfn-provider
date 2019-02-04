# Terraform::Alicloud::MnsTopicSubscription

Provides a MNS topic subscription resource.

~> **NOTE:** Terraform will auto build a mns topic subscription  while it uses `Terraform::Alicloud::MnsTopicSubscription` to build a mns topic subscription resource.

## Properties

`TopicName` - (Required, ForceNew) The topic which The subscription belongs to was named with the name.A topic name must start with an English letter or a digit, and can contain English letters, digits, and hyphens, with the length not exceeding 256 characters.

`Name` - (Required, ForceNew) Two topics subscription on a single account in the same topic cannot have the same name. A topic subscription name must start with an English letter or a digit, and can contain English letters, digits, and hyphens, with the length not exceeding 256 characters.

`NotifyStrategy` - (Optional) The NotifyStrategy attribute of Subscription. This attribute specifies the retry strategy when message sending fails. the attribute has two value EXPONENTIAL_DECAY_RETR or BACKOFF_RETRY. Default value to BACKOFF_RETRY .

`NotifyContentFormat` - (Optional, ForceNew) The NotifyContentFormat attribute of Subscription. This attribute specifies the content format of the messages pushed to users. the attribute has two value SIMPLIFIED or XML.Default value to SIMPLIFIED .

`Endpoint` - (Required, ForceNew) The endpoint has three format. Available values format:
- HTTP Format: http://xxx.com/xxx
- Queue Format: acs:mns:{REGION}:{AccountID}:queues/{QueueName}
- Email Format: mail:directmail:{MailAddress}.

`FilterTag` - (Optional, ForceNew) The length should be shorter than 16.


## Return Values

### Fn::GetAtt

`Id` - The ID of the topic subscription.Format to topic_name:name.

## See Also

* [alicloud_mns_topic_subscription](https://www.terraform.io/docs/providers/alicloud/r/mns_topic_subscription.html) in the _Terraform Provider Documentation_