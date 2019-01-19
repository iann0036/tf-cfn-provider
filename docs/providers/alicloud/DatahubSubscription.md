# Terraform::Alicloud::DatahubSubscription

The subscription is the basic unit of resource usage in Datahub Service under Publish/Subscribe model. You can manage the relationships between user and topics by using subscriptions. [Refer to details](https://help.aliyun.com/document_detail/47440.html).

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the datahub subscritpion as terraform resource. It was composed of project name, topic name and practical subscription ID generated from server side. Format to `<project_name>:<topic_name>:<sub_id>`.

`SubId` - The identidy of the subscritpion, generate from server side.

`CreateTime` - Create time of the datahub subscription. It is a human-readable string rather than 64-bits UTC.

`LastModifyTime` - Last modify time of the datahub subscription. It is the same as *create_time* at the beginning. It is also a human-readable string rather than 64-bits UTC.

## See Also

* [alicloud_datahub_subscription](https://www.terraform.io/docs/providers/alicloud/r/datahub_subscription.html) in the _Terraform Provider Documentation_