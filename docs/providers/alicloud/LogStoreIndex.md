# Terraform::Alicloud::LogStoreIndex

Log Service provides the LogSearch/Analytics function to query and analyze large amounts of logs in real time.
You can use this function by enabling the index and field statistics. [Refer to details](https://www.alibabacloud.com/help/doc-detail/43772.htm)

## Properties

`Project` - (Required, ForceNew) The project name to the log store belongs.

`Logstore` - (Required, ForceNew) The log store name to the query index belongs.

`FullText` - The configuration of full text index. Valid item as follows:.

### FullText Properties

`CaseSensitive` - Whether the case sensitive. Default to false.
* `IncludeChinese` - Whether includes the chinese. Default to false.
* `Token` - The string of several split words, like "\r", "#".

`IncludeChinese` - Whether includes the chinese. Default to false.
* `Token` - The string of several split words, like "\r", "#".

`Token` - The string of several split words, like "\r", "#".

`FieldSearch` - List configurations of field search index. Valid item as follows:.

### FieldSearch Properties

`Name` - (Required) The field name, which is unique in the same log store.
* `Type` - The type of one field. Valid values: ["long", "text", "double", "json"]. Default to "long".
* `Alias` - The alias of one field
* `CaseSensitive` - Whether the case sensitive for the field. Default to false. It is valid when "type" is "text" or "json".
* `IncludeChinese` - Whether includes the chinese for the field. Default to false. It is valid when "type" is "text" or "json".
* `Token` - The string of several split words, like "\r", "#". It is valid when "type" is "text" or "json".
* `EnableAnalytics` - Whether to enable field analytics. Default to true.

`Type` - The type of one field. Valid values: ["long", "text", "double", "json"]. Default to "long".
* `Alias` - The alias of one field
* `CaseSensitive` - Whether the case sensitive for the field. Default to false. It is valid when "type" is "text" or "json".
* `IncludeChinese` - Whether includes the chinese for the field. Default to false. It is valid when "type" is "text" or "json".
* `Token` - The string of several split words, like "\r", "#". It is valid when "type" is "text" or "json".
* `EnableAnalytics` - Whether to enable field analytics. Default to true.

`Alias` - The alias of one field
* `CaseSensitive` - Whether the case sensitive for the field. Default to false. It is valid when "type" is "text" or "json".
* `IncludeChinese` - Whether includes the chinese for the field. Default to false. It is valid when "type" is "text" or "json".
* `Token` - The string of several split words, like "\r", "#". It is valid when "type" is "text" or "json".
* `EnableAnalytics` - Whether to enable field analytics. Default to true.

`CaseSensitive` - Whether the case sensitive for the field. Default to false. It is valid when "type" is "text" or "json".
* `IncludeChinese` - Whether includes the chinese for the field. Default to false. It is valid when "type" is "text" or "json".
* `Token` - The string of several split words, like "\r", "#". It is valid when "type" is "text" or "json".
* `EnableAnalytics` - Whether to enable field analytics. Default to true.

`IncludeChinese` - Whether includes the chinese for the field. Default to false. It is valid when "type" is "text" or "json".
* `Token` - The string of several split words, like "\r", "#". It is valid when "type" is "text" or "json".
* `EnableAnalytics` - Whether to enable field analytics. Default to true.

`Token` - The string of several split words, like "\r", "#". It is valid when "type" is "text" or "json".
* `EnableAnalytics` - Whether to enable field analytics. Default to true.

`EnableAnalytics` - Whether to enable field analytics. Default to true.


## Return Values

### Fn::GetAtt

`Id` - The ID of the log store index. It formats of `<project>:<logstore>`.

`Project` - The project name.

`Logstore` - Log store name.

`FullText` - The full text index config.

`FieldSearch` - The field search index config.

## See Also

* [alicloud_log_store_index](https://www.terraform.io/docs/providers/alicloud/r/log_store_index.html) in the _Terraform Provider Documentation_