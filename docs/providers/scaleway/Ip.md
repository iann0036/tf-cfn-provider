# Terraform::Scaleway::Ip

Provides IPs for servers. This allows IPs to be created, updated and deleted.
For additional details please refer to [API documentation](https://developer.scaleway.com/#ips).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - ID of the new resource.

`Ip` - IP of the new resource.

`Server` - ID of the associated server resource.

`Reverse` - reverse DNS setting of the IP resource.

## See Also

* [scaleway_ip](https://www.terraform.io/docs/providers/scaleway/r/ip.html) in the _Terraform Provider Documentation_