# Terraform::AWS::VpnGateway

Provides a resource to create a VPC VPN Gateway.

## Properties

`VpcId` - (Optional) The VPC ID to create in.

`AvailabilityZone` - (Optional) The Availability Zone for the virtual private gateway.

`Tags` - (Optional) A mapping of tags to assign to the resource.

`AmazonSideAsn` - (Optional) The Autonomous System Number (ASN) for the Amazon side of the gateway. If you don't specify an ASN, the virtual private gateway is created with the default ASN.


## Return Values

### Fn::GetAtt

`Id` - The ID of the VPN Gateway.

## See Also

* [aws_vpn_gateway](https://www.terraform.io/docs/providers/aws/r/vpn_gateway.html) in the _Terraform Provider Documentation_