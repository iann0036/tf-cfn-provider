# Terraform::AWS::NatGateway

Provides a resource to create a VPC NAT Gateway.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the NAT Gateway.

`AllocationId` - The Allocation ID of the Elastic IP address for the gateway.

`SubnetId` - The Subnet ID of the subnet in which the NAT gateway is placed.

`NetworkInterfaceId` - The ENI ID of the network interface created by the NAT gateway.

`PrivateIp` - The private IP address of the NAT Gateway.

`PublicIp` - The public IP address of the NAT Gateway.

## See Also

* [aws_nat_gateway](https://www.terraform.io/docs/providers/aws/r/nat_gateway.html) in the _Terraform Provider Documentation_