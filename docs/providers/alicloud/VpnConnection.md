# Terraform::Alicloud::VpnConnection

Provides a VPN connection resource.

~> **NOTE:** Terraform will auto build vpn connection while it uses `Terraform::Alicloud::VpnConnection` to build a vpn connection resource.
             The vpn connection depends on VPN and VPN customer gateway.

## Properties

`Name` - (Optional) The name of the IPsec connection.

`VpnGatewayId` - (Required ForceNew) The ID of the VPN gateway.

`CustomerGatewayId` - (Required) The ID of the customer gateway.

`LocalSubnet` - (Required, Type:Set) The CIDR block of the VPC to be connected with the local data center. This parameter is used for phase-two negotiation.

`RemoteSubnet` - (Required, Type:Set) The CIDR block of the local data center. This parameter is used for phase-two negotiation.

`EffectImmediately` - (Optional) Whether to delete a successfully negotiated IPsec tunnel and initiate a negotiation again. Valid value:true,false.

`IkeConfig` - (Optional) The configurations of phase-one negotiation.

`IpsecConfig` - (Optional) The configurations of phase-two negotiation.


## Return Values

### Fn::GetAtt

`Id` - The ID of the VPN connection id.

`Status` - The status of VPN connection.

## See Also

* [alicloud_vpn_connection](https://www.terraform.io/docs/providers/alicloud/r/vpn_connection.html) in the _Terraform Provider Documentation_