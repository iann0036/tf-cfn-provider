# Terraform::TencentCloud::NatGateway

Provides a resource to create a VPC NAT Gateway.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the NAT Gateway.

`Name` - The name of the NAT Gateway.

`MaxConcurrent` - The upper limit of concurrent connection of NAT gateway.

`Bandwidth` - The maximum public network output bandwidth of the gateway (unit: Mbps).

`AssignedEipSet` - Elastic IP arrays bound to the gateway.

## See Also

* [tencentcloud_nat_gateway](https://www.terraform.io/docs/providers/tencentcloud/r/nat_gateway.html) in the _Terraform Provider Documentation_