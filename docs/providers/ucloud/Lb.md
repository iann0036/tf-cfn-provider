# Terraform::UCloud::Lb

Provides a Load Balancer resource.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`CreateTime` - The time of creation for load balancer, formatted in RFC3339 time string.

`ExpireTime` - The expiration time for load balancer, formatted in RFC3339 time string.

`IpSet` - It is a nested type which documented below.

`PrivateIp` - The IP address of intranet IP. It is `""` if `internal` is `false`.

`InternetType` - Type of Elastic IP routes.

`Ip` - Elastic IP address.

## See Also

* [ucloud_lb](https://www.terraform.io/docs/providers/ucloud/r/lb.html) in the _Terraform Provider Documentation_