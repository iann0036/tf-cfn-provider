# Terraform::Alicloud::DatahubTopic

The topic is the basic unit of Datahub data source and is used to define one kind of data or stream. It contains a set of subscriptions. You can manage the datahub source of an application by using topics. [Refer to details](https://help.aliyun.com/document_detail/47440.html).

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the datahub topic. It was composed of project name and its name, and formats to `<project_name>:<name>`.

`CreateTime` - Create time of the datahub topic. It is a human-readable string rather than 64-bits UTC.

`LastModifyTime` - Last modify time of the datahub topic. It is the same as *create_time* at the beginning. It is also a human-readable string rather than 64-bits UTC.

## See Also

* [alicloud_datahub_topic](https://www.terraform.io/docs/providers/alicloud/r/datahub_topic.html) in the _Terraform Provider Documentation_