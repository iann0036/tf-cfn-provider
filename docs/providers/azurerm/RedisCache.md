# Terraform::AzureRM::RedisCache

Manages a Redis Cache.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The Route ID.

`Hostname` - The Hostname of the Redis Instance.

`SslPort` - The SSL Port of the Redis Instance.

`Port` - The non-SSL Port of the Redis Instance.

`PrimaryAccessKey` - The Primary Access Key for the Redis Instance.

`SecondaryAccessKey` - The Secondary Access Key for the Redis Instance.

`RedisConfiguration` - A `redis_configuration` block as defined below:.

`Maxclients` - Returns the max number of connected clients at the same time.

## See Also

* [azurerm_redis_cache](https://www.terraform.io/docs/providers/azurerm/r/redis_cache.html) in the _Terraform Provider Documentation_