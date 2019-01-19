# Terraform::Alicloud::VpnGateway

Provides a VPN gateway resource.

-> **NOTE:** Terraform will auto build vpn instance  while it uses `alicloud_vpn_gateway` to build a vpn resource.

-> Currently International-Site account can open `PostPaid` VPN gateway and China-Site account can open `PrePaid` VPN gateway.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the VPN instance id.

`InternetIp` - The internet ip of the VPN.

`Status` - The status of the VPN gateway.

`BusinessStatus` - The business status of the VPN gateway.

## See Also

* [alicloud_vpn_gateway](https://www.terraform.io/docs/providers/alicloud/r/vpn_gateway.html) in the _Terraform Provider Documentation_