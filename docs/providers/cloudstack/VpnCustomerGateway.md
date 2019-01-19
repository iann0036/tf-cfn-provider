# Terraform::CloudStack::VpnCustomerGateway

Creates a site to site VPN local customer gateway.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the VPN Customer Gateway.

`Dpd` - Enable or disable DPD is enabled for the related VPN connection.

`EspLifetime` - The ESP lifetime of phase 2 VPN connection to this VPN Customer Gateway.

`IkeLifetime` - The IKE lifetime of phase 2 VPN connection to this VPN Customer Gateway.

## See Also

* [cloudstack_vpn_customer_gateway](https://www.terraform.io/docs/providers/cloudstack/r/vpn_customer_gateway.html) in the _Terraform Provider Documentation_