# Terraform::Alicloud::LogStore

The log store is a unit in Log Service to collect, store, and query the log data. Each log store belongs to a project,
and each project can create multiple Logstores. [Refer to details](https://www.alibabacloud.com/help/doc-detail/48874.htm)

## Properties

`Project` - (Required, ForceNew) The project name to the log store belongs.

`Name` - (Required, ForceNew) The log store, which is unique in the same project.

`RetentionPeriod` - The data retention time (in days). Valid values: [1-3650]. Default to 30. Log store data will be stored permanently when the value is "3650".

`ShardCount` - The number of shards in this log store. Default to 2. You can modify it by "Split" or "Merge" operations. [Refer to details](https://www.alibabacloud.com/help/doc-detail/28976.htm).

`AutoSplit` - Determines whether to automatically split a shard. Default to true.

`MaxSplitShardCount` - The maximum number of shards for automatic split, which is in the range of 1 to 64. You must specify this parameter when autoSplit is true.

`AppendMeta` - Determines whether to append log meta automatically. The meta includes log receive time and client IP address. Default to true.

`EnableWebTracking` - Determines whether to enable Web Tracking. Default false.


## Return Values

### Fn::GetAtt

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