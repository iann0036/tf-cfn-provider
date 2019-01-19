# Terraform::AWS::Ec2TransitGatewayRoute

Manages an EC2 Transit Gateway Route.

## Properties

`DestinationCidrBlock` - (Required) IPv4 CIDR range used for destination matches. Routing decisions are based on the most specific match.

`TransitGatewayAttachmentId` - (Required) Identifier of EC2 Transit Gateway Attachment.

`TransitGatewayRouteTableId` - (Required) Identifier of EC2 Transit Gateway Route Table.


## See Also

* [aws_ec2_transit_gateway_route](https://www.terraform.io/docs/providers/aws/r/ec2_transit_gateway_route.html) in the _Terraform Provider Documentation_