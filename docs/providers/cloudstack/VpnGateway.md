# Terraform::CloudStack::VpnGateway

Creates a site to site VPN local gateway.

## Properties

`VpcId` - (Required) The ID of the VPC for which to create the VPN Gateway. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The ID of the VPN Gateway.

`PublicIp` - The public IP address associated with the VPN Gateway.

## See Also

* [cloudstack_vpn_gateway](https://www.terraform.io/docs/providers/cloudstack/r/vpn_gateway.html) in the _Terraform Provider Documentation_