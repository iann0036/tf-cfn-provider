# Terraform::UCloud::Lb

Provides a Load Balancer resource.

## Properties

`Internal` - (Optional) Indicate whether the load balancer is intranet.

`ChargeType` - (Optional) Charge type of load balancer. Possible values are: `year` as pay by year, `month` as pay by month, `dynamic` as pay by hour (specific permission required). (Default: `month`).

`Name` - (Optional) The name of the load balancer. If not specified, terraform will autogenerate a name beginning with `tf-lb`.

`VpcId` - (Optional) The ID of the VPC linked to the Load Balancers, This argumnet is not required if default VPC.

`SubnetId` - (Optional) The ID of subnet that intrant load balancer belongs to. This argumnet is not required if default subnet.

`Tag` - (Optional) A mapping of tags to assign to VPC, which contains at most 63 characters and only support Chinese, English, numbers, '-', '_', and '.'. If it is not filled in or a empty string is filled in, then default tag will be assigned. (Default: `Default`).

`Remark` - (Optional) The remarks of the load balancer. (Default: is `""`).


## Return Values

### Fn::GetAtt

`CreateTime` - The time of creation for load balancer, formatted in RFC3339 time string.

`ExpireTime` - The expiration time for load balancer, formatted in RFC3339 time string.

`IpSet` - It is a nested type which documented below.

`PrivateIp` - The IP address of intranet IP. It is `""` if `Internal` is `false`.

`InternetType` - Type of Elastic IP routes.

`Ip` - Elastic IP address.

## See Also

* [ucloud_lb](https://www.terraform.io/docs/providers/ucloud/r/lb.html) in the _Terraform Provider Documentation_