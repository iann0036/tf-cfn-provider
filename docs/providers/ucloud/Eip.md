# Terraform::UCloud::Eip

Provides an Elastic IP resource.

## Properties

`InternetType` - (Required) Type of Elastic IP routes. Possible values are: `international` as internaltional BGP IP and `bgp` as china BGP IP.

`Bandwidth` - (Optional) Maximum bandwidth to the elastic public network, measured in Mbps (Mega bit per second). the ranges for bandwidth are: 1-200 for pay by traffic, 1-800 for pay by bandwith. (Default: `1`).

`Duration` - (Optional) The duration that you will buy the resource. (Default: `1`). It is not required when `dynamic` (pay by hour), the value is `0` when `month`(pay by month) and the instance will be vaild till the last day of that month.

`ChargeType` - (Optional) Elastic IP charge type. Possible values are: `year` as pay by year, `month` as pay by month, `dynamic` as pay by hour (specific permission required). (Default: `month`).

`Name` - (Optional) The name of the EIP, which contains 1-63 characters and only support Chinese, English, numbers, '-', '_', '.'. If not specified, terraform will autogenerate a name beginning with `tf-eip`.

`Remark` - (Optional) The remarks of the EIP. (Default: `""`).

`Tag` - (Optional) A mapping of tags to assign to VPC, which contains at most 63 characters and only support Chinese, English, numbers, '-', '_', and '.'. If it is not filled in or a empty string is filled in, then default tag will be assigned. (Default: `Default`).


## Return Values

### Fn::GetAtt

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