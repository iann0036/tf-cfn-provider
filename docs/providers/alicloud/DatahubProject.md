# Terraform::Alicloud::DatahubProject

The project is the basic unit of resource management in Datahub Service and is used to isolate and control resources. It contains a set of Topics. You can manage the datahub sources of an application by using projects. [Refer to details](https://help.aliyun.com/document_detail/47440.html).

-> **NOTE:** Currently Datahub service only can be supported in the regions: cn-beijing, cn-hangzhou, cn-shanghai, cn-shenzhen,  ap-southeast-1.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the datahub project. It is the same as its name.

`CreateTime` - Create time of the datahub project. It is a human-readable string rather than 64-bits UTC.

`LastModifyTime` - Last modify time of the datahub project. It is the same as *create_time* at the beginning. It is also a human-readable string rather than 64-bits UTC.

## See Also

* [alicloud_datahub_project](https://www.terraform.io/docs/providers/alicloud/r/datahub_project.html) in the _Terraform Provider Documentation_