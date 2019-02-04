# Terraform::Alicloud::DatahubTopic

The topic is the basic unit of Datahub data source and is used to define one kind of data or stream. It contains a set of subscriptions. You can manage the datahub source of an application by using topics. [Refer to details](https://help.aliyun.com/document_detail/47440.html).

## Properties

`Name` - (Required, ForceNew) The name of the datahub topic. Its length is limited to 1-128 and only characters such as letters, digits and '_' are allowed. It is case-insensitive.

`ProjectName` - (Required, ForceNew) The name of the datahub project that this topic belongs to. It is case-insensitive.

`ShardCount` - (Optional) The number of shards this topic contains. The permitted range of values is [1, 10]. The default value is 1.

`LifeCycle` - (Optional) How many days this topic lives. The permitted range of values is [1, 7]. The default value is 3.

`RecordType` - (Optional) The type of this topic. Its value must be one of {BLOB, TUPLE}. For BLOB topic, data will be organized as binary and encoded by BASE64. For TUPLE topic, data has fixed schema. The default value is "TUPLE" with a schema {STRING}.

`RecordSchema` - (Optional) Schema of this topic, required only for TUPLE topic. Supported data types (case-insensitive) are:
- BIGINT
- STRING
- BOOLEAN
- DOUBLE
- TIMESTAMP.

`Comment` - (Optional) Comment of the datahub topic. It cannot be longer than 255 characters.


## Return Values

### Fn::GetAtt

`Id` - The ID of the datahub topic. It was composed of project name and its name, and formats to `<project_name>:<name>`.

`CreateTime` - Create time of the datahub topic. It is a human-readable string rather than 64-bits UTC.

`LastModifyTime` - Last modify time of the datahub topic. It is the same as *create_time* at the beginning. It is also a human-readable string rather than 64-bits UTC.

## See Also

* [alicloud_datahub_topic](https://www.terraform.io/docs/providers/alicloud/r/datahub_topic.html) in the _Terraform Provider Documentation_