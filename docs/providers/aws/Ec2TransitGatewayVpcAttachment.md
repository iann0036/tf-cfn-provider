# Terraform::AWS::Ec2TransitGatewayVpcAttachment

Manages an EC2 Transit Gateway VPC Attachment. For examples of custom route table association and propagation, see the EC2 Transit Gateway Networking Examples Guide.

## Properties

`SubnetIds` - (Required) Identifiers of EC2 Subnets.

`TransitGatewayId` - (Required) Identifier of EC2 Transit Gateway.

`VpcId` - (Required) Identifier of EC2 VPC.

`DnsSupport` - (Optional) Whether DNS support is enabled. Valid values: `disable`, `enable`. Default value: `enable`.

`Ipv6Support` - (Optional) Whether IPv6 support is enabled. Valid values: `disable`, `enable`. Default value: `disable`.

`Tags` - (Optional) Key-value tags for the EC2 Transit Gateway VPC Attachment.

`TransitGatewayDefaultRouteTableAssociation` - (Optional) Boolean whether the VPC Attachment should be associated with the EC2 Transit Gateway association default route table. Default value: `true`.

`TransitGatewayDefaultRouteTablePropagation` - (Optional) Boolean whether the VPC Attachment should propagate routes with the EC2 Transit Gateway propagation default route table. Default value: `true`.


## See Also

* [aws_ec2_transit_gateway_vpc_attachment](https://www.terraform.io/docs/providers/aws/r/ec2_transit_gateway_vpc_attachment.html) in the _Terraform Provider Documentation_