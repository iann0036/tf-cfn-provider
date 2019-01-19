# Terraform::AWS::VpnConnection

Manages an EC2 VPN connection. These objects can be connected to customer gateways, and allow you to establish tunnels between your network and Amazon.

~> **Note:** All arguments including `Tunnel1PresharedKey` and `Tunnel2PresharedKey` will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

~> **Note:** The CIDR blocks in the arguments `Tunnel1InsideCidr` and `Tunnel2InsideCidr` must have a prefix of /30 and be a part of a specific range.
[Read more about this in the AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_VpnTunnelOptionsSpecification.html).

## Properties

`CustomerGatewayId` - (Required) The ID of the customer gateway.

`Type` - (Required) The type of VPN connection. The only type AWS supports at this time is "ipsec.1".

`TransitGatewayId` - (Optional) The ID of the EC2 Transit Gateway.

`VpnGatewayId` - (Optional) The ID of the Virtual Private Gateway.

`StaticRoutesOnly` - (Optional, Default `false`) Whether the VPN connection uses static routes exclusively. Static routes must be used for devices that don't support BGP.

`Tags` - (Optional) Tags to apply to the connection.

`Tunnel1InsideCidr` - (Optional) The CIDR block of the inside IP addresses for the first VPN tunnel.

`Tunnel2InsideCidr` - (Optional) The CIDR block of the second IP addresses for the first VPN tunnel.

`Tunnel1PresharedKey` - (Optional) The preshared key of the first VPN tunnel.

`Tunnel2PresharedKey` - (Optional) The preshared key of the second VPN tunnel.


## See Also

* [aws_vpn_connection](https://www.terraform.io/docs/providers/aws/r/vpn_connection.html) in the _Terraform Provider Documentation_