# Terraform::Scaleway::IpReverseDns

Provides reverse DNS settings for IPs.
For additional details please refer to [API documentation](https://developer.scaleway.com/#ips).

## Properties

`Ip` - (Required) ID or Address of IP.

`Reverse` - (Required) Reverse DNS of the IP.


## Return Values

### Fn::GetAtt

`Id` - ID of the new resource.

`Reverse` - reverse DNS setting of the IP resource.

## See Also

* [scaleway_ip_reverse_dns](https://www.terraform.io/docs/providers/scaleway/r/ip_reverse_dns.html) in the _Terraform Provider Documentation_