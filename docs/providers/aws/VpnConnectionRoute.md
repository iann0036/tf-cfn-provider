# Terraform::AWS::VpnConnectionRoute

Provides a static route between a VPN connection and a customer gateway.

## Properties

`DestinationCidrBlock` - (Required) The CIDR block associated with the local subnet of the customer network.

`VpnConnectionId` - (Required) The ID of the VPN connection.


## See Also

* [aws_vpn_connection_route](https://www.terraform.io/docs/providers/aws/r/vpn_connection_route.html) in the _Terraform Provider Documentation_