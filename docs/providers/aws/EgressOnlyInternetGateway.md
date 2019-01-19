# Terraform::AWS::EgressOnlyInternetGateway

[IPv6 only] Creates an egress-only Internet gateway for your VPC.
An egress-only Internet gateway is used to enable outbound communication
over IPv6 from instances in your VPC to the Internet, and prevents hosts
outside of your VPC from initiating an IPv6 connection with your instance.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the Egress Only Internet Gateway.

## See Also

* [aws_egress_only_internet_gateway](https://www.terraform.io/docs/providers/aws/r/egress_only_internet_gateway.html) in the _Terraform Provider Documentation_