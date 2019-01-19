# Terraform::UCloud::Eip

Provides an Elastic IP resource.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`CreateTime` - The time of creation for EIP, formatted in RFC3339 time string.

`ExpireTime` - The expiration time for EIP, formatted in RFC3339 time string.

`IpSet` - It is a nested type which documented below.

`Resource` - It is a nested type which documented below.

`Status` - EIP status. Possible values are: `used` as in use, `free` as available and `freeze` as associating.

`PublicIp` - Public IP address of Elastic IP.

`InternetType` - Type of Elastic IP routes.

`Id` - The ID of the resource with EIP attached.

`Type` - The type of resource with EIP attached. Possible values are `instance` as instance, `vrouter` as visual router, `lb` as load balancer.

## See Also

* [ucloud_eip](https://www.terraform.io/docs/providers/ucloud/r/eip.html) in the _Terraform Provider Documentation_