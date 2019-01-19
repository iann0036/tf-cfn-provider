# Terraform::HuaweiCloud::DmsQueueV1

Manages a DMS queue in the huaweicloud DMS Service.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Name` - See Argument Reference above.

`QueueMode` - See Argument Reference above.

`Description` - See Argument Reference above.

`RedrivePolicy` - See Argument Reference above.

`MaxConsumeCount` - See Argument Reference above.

`Created` - Indicates the time when a queue is created.

`Reservation` - Indicates the retention period (unit: min) of a message in a queue.

`MaxMsgSizeByte` - Indicates the maximum message size (unit: byte) that is allowed in queue.

`ProducedMessages` - Indicates the total number of messages (not including the messages that have expired and been deleted) in a queue.

`GroupCount` - Indicates the total number of consumer groups in a queue.

## See Also

* [huaweicloud_dms_queue_v1](https://www.terraform.io/docs/providers/huaweicloud/r/dms_queue_v1.html) in the _Terraform Provider Documentation_