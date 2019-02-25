# Terraform::FlexibleEngine::SmnTopicV2

Manages a V2 topic resource within FlexibleEngine.

## Properties

`Name` - (Required) The name of the topic to be created.

`DisplayName` - (Optional) Topic display name, which is presented as the
name of the email sender in an email message.


## Return Values

### Fn::GetAtt

`Name` - See Properties above.

`DisplayName` - See Properties above.

`TopicUrn` - Resource identifier of a topic, which is unique.

`PushPolicy` - Message pushing policy. 0 indicates that the message.

`CreateTime` - Time when the topic was created.

`UpdateTime` - Time when the topic was updated.

## See Also

* [flexibleengine_smn_topic_v2](https://www.terraform.io/docs/providers/flexibleengine/r/smn_topic_v2.html) in the _Terraform Provider Documentation_