# Terraform::OpenTelekomCloud::DmsQueueV2

Manages a DMS queue in the opentelekomcloud DMS Service.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

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

* [opentelekomcloud_dms_queue_v2](https://www.terraform.io/docs/providers/opentelekomcloud/r/dms_queue_v2.html) in the _Terraform Provider Documentation_