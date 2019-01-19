# Terraform::Alicloud::LogStoreIndex

Log Service provides the LogSearch/Analytics function to query and analyze large amounts of logs in real time.
You can use this function by enabling the index and field statistics. [Refer to details](https://www.alibabacloud.com/help/doc-detail/43772.htm)

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the log store index. It formats of `<project>:<logstore>`.

`Project` - The project name.

`Logstore` - Log store name.

`FullText` - The full text index config.

`FieldSearch` - The field search index config.

## See Also

* [alicloud_log_store_index](https://www.terraform.io/docs/providers/alicloud/r/log_store_index.html) in the _Terraform Provider Documentation_