# Terraform::AWS::Route

Provides a resource to create a routing table entry (a route) in a VPC routing table.

~> **NOTE on Route Tables and Routes:** Terraform currently
provides both a standalone Route resource and a [Route Table](route_table.html) resource with routes
defined in-line. At this time you cannot use a Route Table with in-line routes
in conjunction with any Route resources. Doing so will cause
a conflict of rule settings and will overwrite rules.

## Properties

`RouteTableId` - (Required) The ID of the routing table.

`DestinationCidrBlock` - (Optional) The destination CIDR block.

`DestinationIpv6CidrBlock` - (Optional) The destination IPv6 CIDR block.

`EgressOnlyGatewayId` - (Optional) Identifier of a VPC Egress Only Internet Gateway.

`GatewayId` - (Optional) Identifier of a VPC internet gateway or a virtual private gateway.

`InstanceId` - (Optional) Identifier of an EC2 instance.

`NatGatewayId` - (Optional) Identifier of a VPC NAT gateway.

`NetworkInterfaceId` - (Optional) Identifier of an EC2 network interface.

`TransitGatewayId` - (Optional) Identifier of an EC2 Transit Gateway.

`VpcPeeringConnectionId` - (Optional) Identifier of a VPC peering connection.


## Return Values

### Fn::GetAtt

`Id` - Route Table identifier and destination.

## See Also

* [aws_route](https://www.terraform.io/docs/providers/aws/r/route.html) in the _Terraform Provider Documentation_