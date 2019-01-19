# Terraform::TelefonicaOpenCloud::MaasTaskV1

Manages resource task within TelefonicaOpenCloud MAAS.

## Properties

`SrcNode` - (Required) Specifies the source node information.

`DstNode` - (Required) Specifies the destination node information.

`EnableKms` - (Required) Specifies whether to use KMS encryption.

`ThreadNum` - (Required) Specifies the number of threads used by the migration task. The value cannot exceed 50.

`Description` - (Optional) Specifies tasks description, which cannot exceed 255 characters. The following special characters are not allowed: <>()"&.

`SmnInfo` - (Optional) Specifies the field used for sending messages using the Simple Message Notification (SMN) service.

`Region` - (Required) Specifies the region where the destination bucket locates.

`Ak` - (Required) Specifies the destination bucket Access Key.

`Sk` - (Required) Specifies the destination bucket Secret Key.

`ObjectKey` - (Optional) Specifies the name of the object to be selected in the destination bucket.

`Bucket` - (Required) Specifies the name of the destination bucket.

`CloudType` - (Optional) Specifies the source cloud vendor. The default value is AWS and only AWS is supported now.

`TopicUrn` - (Required) Specifies the SMN message topic URN bound to a migration task.

`Language` - (Optional) Specifies the management console language used by the current users. Users can select en-us.

`TriggerConditions` - (Required) Specifies the trigger conditions of sending messages using SMN. The value depending on the state of a migration task. The migration task status can be SUCCESS or FAIL.


## Return Values

### Fn::GetAtt

`SrcNode` - See Properties above.

`DstNode` - See Properties above.

`EnableKms` - See Properties above.

`ThreadNum` - See Properties above.

`Description` - See Properties above.

`SmnInfo` - See Properties above.

`Name` - Specifies the name for a task.

`Status` - Specifies the task status as follows: 0: Not started, 1: Waiting to migrate,.

## See Also

* [telefonicaopencloud_maas_task_v1](https://www.terraform.io/docs/providers/telefonicaopencloud/r/maas_task_v1.html) in the _Terraform Provider Documentation_