# Terraform::CloudStack::VpnCustomerGateway

Creates a site to site VPN local customer gateway.

## Properties

`Name` - (Required) The name of the VPN Customer Gateway.

`Cidr` - (Required) The CIDR block that needs to be routed through this gateway.

`EspPolicy` - (Required) The ESP policy to use for this VPN Customer Gateway.

`Gateway` - (Required) The public IP address of the related VPN Gateway.

`IkePolicy` - (Required) The IKE policy to use for this VPN Customer Gateway.

`IpsecPsk` - (Required) The IPSEC pre-shared key used for this gateway.

`Dpd` - (Optional) If DPD is enabled for the related VPN connection (defaults false).

`EspLifetime` - (Optional) The ESP lifetime of phase 2 VPN connection to this VPN Customer Gateway in seconds (defaults 86400).

`IkeLifetime` - (Optional) The IKE lifetime of phase 2 VPN connection to this VPN Customer Gateway in seconds (defaults 86400).

`Project` - (Optional) The name or ID of the project to create this VPN Customer Gateway in. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The ID of the VPN Customer Gateway.

`Dpd` - Enable or disable DPD is enabled for the related VPN connection.

`EspLifetime` - The ESP lifetime of phase 2 VPN connection to this VPN Customer Gateway.

`IkeLifetime` - The IKE lifetime of phase 2 VPN connection to this VPN Customer Gateway.

## See Also

* [cloudstack_vpn_customer_gateway](https://www.terraform.io/docs/providers/cloudstack/r/vpn_customer_gateway.html) in the _Terraform Provider Documentation_