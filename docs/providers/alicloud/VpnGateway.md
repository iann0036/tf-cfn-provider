# Terraform::Alicloud::VpnGateway

Provides a VPN gateway resource.

-> **NOTE:** Terraform will auto build vpn instance  while it uses `Terraform::Alicloud::VpnGateway` to build a vpn resource.

-> Currently International-Site account can open `PostPaid` VPN gateway and China-Site account can open `PrePaid` VPN gateway.

## Properties

`Name` - (Optional) The name of the VPN. Defaults to null.

`VpcId` - (Required, Forces new resource) The VPN belongs the vpc_id, the field can't be changed.

`InstanceChargeType` - (Optional) The charge type for instance. Valid value: PostPaid, PrePaid. Default to PostPaid.

`Period` - (Optional) The filed is only required while the InstanceChargeType is prepaid.

`Bandwidth` - (Required) The value should be 10, 100, 200, 500, 1000 if the user is postpaid, otherwise it can be 5, 10, 20, 50, 100, 200, 500, 1000. It can't be changed by terraform.

`EnableIpsec` - (Optional) Enable or Disable IPSec VPN. At least one type of VPN should be enabled.

`EnableSsl` - (Optional) Enable or Disable SSL VPN.  At least one type of VPN should be enabled.

`SslConnections` - (Optional) The max connections of SSL VPN. Default to 5.

`Description` - (Optional) The description of the VPN instance.


## Return Values

### Fn::GetAtt

`Id` - The ID of the VPN instance id.

`InternetIp` - The internet ip of the VPN.

`Status` - The status of the VPN gateway.

`BusinessStatus` - The business status of the VPN gateway.

## See Also

* [alicloud_vpn_gateway](https://www.terraform.io/docs/providers/alicloud/r/vpn_gateway.html) in the _Terraform Provider Documentation_