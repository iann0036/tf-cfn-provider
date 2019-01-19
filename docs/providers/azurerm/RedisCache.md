# Terraform::AzureRM::RedisCache

Manages a Redis Cache.

## Properties

`Name` - (Required) The name of the Redis instance. Changing this forces a new resource to be created.

`Location` - (Required) The location of the resource group.

`ResourceGroupName` - (Required) The name of the resource group in which to create the Redis instance.

`Capacity` - (Required) The size of the Redis cache to deploy. Valid values for a SKU `Family` of C (Basic/Standard) are `0, 1, 2, 3, 4, 5, 6`, and for P (Premium) `Family` are `1, 2, 3, 4`.

`Family` - (Required) The SKU family to use. Valid values are `C` and `P`, where C = Basic/Standard, P = Premium.

`SkuName` - (Required) The SKU of Redis to use - can be either Basic, Standard or Premium.

`EnableNonSslPort` - (Optional) Enable the non-SSL port (6789) - disabled by default.

`PatchSchedule` - (Optional) A list of `PatchSchedule` blocks as defined below - only available for Premium SKU's.

`PrivateStaticIpAddress` - (Optional) The Static IP Address to assign to the Redis Cache when hosted inside the Virtual Network. Changing this forces a new resource to be created.

`RedisConfiguration` - (Required) A `RedisConfiguration` as defined below - with some limitations by SKU - defaults/details are shown below.

`ShardCount` - (Optional) *Only available when using the Premium SKU* The number of Shards to create on the Redis Cluster.

`SubnetId` - (Optional) The ID of the Subnet within which the Redis Cache should be deployed. Changing this forces a new resource to be created.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`Zones` - (Optional) A list of a single item of the Availability Zone which the Redis Cache should be allocated in.

### RedisConfiguration Properties

`MaxmemoryReserved` - (Optional) Value in megabytes reserved for non-cache usage e.g. failover. Defaults are shown below.

`MaxmemoryDelta` - (Optional) The max-memory delta for this Redis instance. Defaults are shown below.

`MaxmemoryPolicy` - (Optional) How Redis will select what to remove when `maxmemory` is reached. Defaults are shown below.

`RdbBackupEnabled` - (Optional) Is Backup Enabled? Only supported on Premium SKU's.

`RdbBackupFrequency` - (Optional) The Backup Frequency in Minutes. Only supported on Premium SKU's. Possible values are: `15`, `30`, `60`, `360`, `720` and `1440`.

`RdbBackupMaxSnapshotCount` - (Optional) The maximum number of snapshots to create as a backup. Only supported for Premium SKU's.

`RdbStorageConnectionString` - (Optional) The Connection String to the Storage Account. Only supported for Premium SKU's. In the format: `DefaultEndpointsProtocol=https;BlobEndpoint=${azurerm_storage_account.test.primary_blob_endpoint};AccountName=${azurerm_storage_account.test.name};AccountKey=${azurerm_storage_account.test.primary_access_key}`.

`NotifyKeyspaceEvents` - (Optional) Keyspace notifications allows clients to subscribe to Pub/Sub channels in order to receive events affecting the Redis data set in some way. [Reference](https://redis.io/topics/notifications#configuration).


## Return Values

### Fn::GetAtt

`Id` - The Route ID.

`Hostname` - The Hostname of the Redis Instance.

`SslPort` - The SSL Port of the Redis Instance.

`Port` - The non-SSL Port of the Redis Instance.

`PrimaryAccessKey` - The Primary Access Key for the Redis Instance.

`SecondaryAccessKey` - The Secondary Access Key for the Redis Instance.

`RedisConfiguration` - A `RedisConfiguration` block as defined below:.

`Maxclients` - Returns the max number of connected clients at the same time.

## See Also

* [azurerm_redis_cache](https://www.terraform.io/docs/providers/azurerm/r/redis_cache.html) in the _Terraform Provider Documentation_