# Terraform::AWS::VpnGatewayRoutePropagation

Requests automatic route propagation between a VPN gateway and a route table.

~> **Note:** This resource should not be used with a route table that has
the `propagating_vgws` argument set. If that argument is set, any route
propagation not explicitly listed in its value will be removed.

## Properties

TBC

## See Also

* [aws_vpn_gateway_route_propagation](https://www.terraform.io/docs/providers/aws/r/vpn_gateway_route_propagation.html) in the _Terraform Provider Documentation_