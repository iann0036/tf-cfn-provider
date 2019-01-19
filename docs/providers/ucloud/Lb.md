# Terraform::UCloud::Lb

Provides a Load Balancer resource.

## Properties

TBC

## Return Values

### Fn::GetAtt

`CreateTime` - The time of creation for load balancer, formatted in RFC3339 time string.

`ExpireTime` - The expiration time for load balancer, formatted in RFC3339 time string.

`IpSet` - It is a nested type which documented below.

`PrivateIp` - The IP address of intranet IP. It is `""` if `internal` is `false`.

`InternetType` - Type of Elastic IP routes.

`Ip` - Elastic IP address.

## See Also

* [ucloud_lb](https://www.terraform.io/docs/providers/ucloud/r/lb.html) in the _Terraform Provider Documentation_