# Terraform::Alicloud::LogtailConfig

The Logtail access service is a log collection agent provided by Log Service. 
You can use Logtail to collect logs from servers such as Alibaba Cloud Elastic
Compute Service (ECS) instances in real time in the Log Service console. [Refer to details](https://www.alibabacloud.com/help/doc-detail/29058.htm
)

## Properties

`Project` - (Required, ForceNew) The project name to the log store belongs.

`Logstore` - (Required, ForceNew) The log store name to the query index belongs.

`InputType` - (Required) The input type. Currently only two types of files and plugin are supported.

`LogSample` - （Optional）The log sample of the Logtail configuration. The log size cannot exceed 1,000 bytes.

`ConfigName` - (Required, ForceNew) The Logtail configuration name, which is unique in the same project.

`OutputType` - (Required) The output type. Currently, only LogService is supported.

`InputDetail` - (Required) The logtail configure the required JSON files.([Refer to details](https://www.alibabacloud.com/help/doc-detail/29058.htm)).


## Return Values

### Fn::GetAtt

`Id` - The ID of the log store index. It formats of `<project>:<logstore>:<config_name>`.

## See Also

* [alicloud_logtail_config](https://www.terraform.io/docs/providers/alicloud/r/logtail_config.html) in the _Terraform Provider Documentation_