# Terraform::Scaleway::Ip

Provides IPs for servers. This allows IPs to be created, updated and deleted.
For additional details please refer to [API documentation](https://developer.scaleway.com/#ips).

## Properties

`Server` - (Optional) ID of server to associate IP with.

`Reverse` - (Deprecated) Please us the scaleway_ip_reverse_dns resource instead.


## Return Values

### Fn::GetAtt

`Id` - ID of the new resource.

`Ip` - IP of the new resource.

`Server` - ID of the associated server resource.

`Reverse` - reverse DNS setting of the IP resource.

## See Also

* [scaleway_ip](https://www.terraform.io/docs/providers/scaleway/r/ip.html) in the _Terraform Provider Documentation_