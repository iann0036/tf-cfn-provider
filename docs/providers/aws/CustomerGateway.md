# Terraform::AWS::CustomerGateway

Provides a customer gateway inside a VPC. These objects can be connected to VPN gateways via VPN connections, and allow you to establish tunnels between your network and the VPC.

## Properties

`BgpAsn` - (Required) The gateway's Border Gateway Protocol (BGP) Autonomous System Number (ASN).

`IpAddress` - (Required) The IP address of the gateway's Internet-routable external interface.

`Type` - (Required) The type of customer gateway. The only type AWS supports at this time is "ipsec.1".

`Tags` - (Optional) Tags to apply to the gateway.


## See Also

* [aws_customer_gateway](https://www.terraform.io/docs/providers/aws/r/customer_gateway.html) in the _Terraform Provider Documentation_