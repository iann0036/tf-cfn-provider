# Terraform::TencentCloud::NatGateway

Provides a resource to create a VPC NAT Gateway.

## Properties

`Name` - (Required) The name for the NAT Gateway.

`VpcId` - (Required, Forces new resource) The VPC ID.

`MaxConcurrent` - (Required) The upper limit of concurrent connection of NAT gateway, for example: 1000000, 3000000, 10000000. To learn more, please refer to [Virtual Private Cloud Gateway Description](https://intl.cloud.tencent.com/doc/product/215/1682).

`Bandwidth` - (Required) The maximum public network output bandwidth of the gateway (unit: Mbps), for example: 10, 20, 50, 100, 200, 500, 1000, 2000, 5000. For more information, please refer to [Virtual Private Cloud Gateway Description](https://intl.cloud.tencent.com/doc/product/215/1682).

`AssignedEipSet` - (Required) Elastic IP arrays bound to the gateway, For more information on elastic IP, please refer to [Elastic IP](eip.html).


## Return Values

### Fn::GetAtt

`Id` - The ID of the NAT Gateway.

`Name` - The name of the NAT Gateway.

`MaxConcurrent` - The upper limit of concurrent connection of NAT gateway.

`Bandwidth` - The maximum public network output bandwidth of the gateway (unit: Mbps).

`AssignedEipSet` - Elastic IP arrays bound to the gateway.

## See Also

* [tencentcloud_nat_gateway](https://www.terraform.io/docs/providers/tencentcloud/r/nat_gateway.html) in the _Terraform Provider Documentation_