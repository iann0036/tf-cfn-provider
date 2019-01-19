# Terraform::Alicloud::VpnConnection

Provides a VPN connection resource.

~> **NOTE:** Terraform will auto build vpn connection while it uses `alicloud_vpn_connection` to build a vpn connection resource.
             The vpn connection depends on VPN and VPN customer gateway.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the VPN connection id.

`Status` - The status of VPN connection.

## See Also

* [alicloud_vpn_connection](https://www.terraform.io/docs/providers/alicloud/r/vpn_connection.html) in the _Terraform Provider Documentation_