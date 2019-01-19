# Terraform::HuaweiCloud::CtsTrackerV1

Allows you to collect, store, and query cloud resource operation records.

## Properties

`BucketName` - (Required) The OBS bucket name for a tracker.

`FilePrefixName` - (Optional) The prefix of a log that needs to be stored in an OBS bucket.

`IsSupportSmn` - (Required) Specifies whether SMN is supported. When the value is false, topic_id and operations can be left empty.

`TopicId` - (Required)The theme of the SMN service, Is obtained from SMN and in the format of **urn:smn:([a-z]|[A-Z]|[0-9]|\-){1,32}:([a-z]|[A-Z]|[0-9]){32}:([a-z]|[A-Z]|[0-9]|\-|\_){1,256}**.

`Operations` - (Required) Trigger conditions for sending a notification.

`IsSendAllKeyOperation` - (Required) When the value is **false**, operations cannot be left empty.

`NeedNotifyUserList` - (Optional) The users using the login function. When these users log in, notifications will be sent.


## Return Values

### Fn::GetAtt

`Status` - The status of a tracker. The value is **enabled**.

`TrackerName` - The tracker name. Currently, only tracker **system** is available.

## See Also

* [huaweicloud_cts_tracker_v1](https://www.terraform.io/docs/providers/huaweicloud/r/cts_tracker_v1.html) in the _Terraform Provider Documentation_