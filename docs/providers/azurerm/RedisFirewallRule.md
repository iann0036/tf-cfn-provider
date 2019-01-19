# Terraform::AzureRM::RedisFirewallRule

Manages a Firewall Rule associated with a Redis Cache.

## Properties

`Name` - (Required) The name of the Firewall Rule. Changing this forces a new resource to be created.

`RedisCacheName` - (Required) The name of the Redis Cache. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which this Redis Cache exists.

`StartIp` - (Required) The lowest IP address included in the range.

`EndIp` - (Required) The highest IP address included in the range.


## Return Values

### Fn::GetAtt

`Id` - The Redis Firewall Rule ID.

## See Also

* [azurerm_redis_firewall_rule](https://www.terraform.io/docs/providers/azurerm/r/redis_firewall_rule.html) in the _Terraform Provider Documentation_