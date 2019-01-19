# Terraform::Alicloud::LogStore

The log store is a unit in Log Service to collect, store, and query the log data. Each log store belongs to a project,
and each project can create multiple Logstores. [Refer to details](https://www.alibabacloud.com/help/doc-detail/48874.htm)

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the log project. It formats of `<project>:<name>`.

`Project` - The project name.

`Name` - Log store name.

`RetentionPeriod` - The data retention time.

`ShardCount` - The number of shards.

`AutoSplit` - Determines whether to automatically split a shard.

`MaxSplitShardCount` - The maximum number of shards for automatic split.

`AppendMeta` - Determines whether to append log meta automatically.

`EnableWebTracking` - Determines whether to enable Web Tracking.

## See Also

* [alicloud_log_store](https://www.terraform.io/docs/providers/alicloud/r/log_store.html) in the _Terraform Provider Documentation_