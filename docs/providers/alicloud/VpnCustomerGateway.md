# Terraform::Alicloud::VpnCustomerGateway

Provides a VPN customer gateway resource.

~> **NOTE:** Terraform will auto build vpn customer gateway instance  while it uses `Terraform::Alicloud::VpnCustomerGateway` to build a vpn customer gateway resource.

## Properties

`Name` - (Optional) The name of the VPN customer gateway. Defaults to null.

`IpAddress` - (Required, Forces new resource) The IP address of the customer gateway.

`Description` - (Optional) The description of the VPN customer gateway instance.


## Return Values

### Fn::GetAtt

`Id` - The ID of the VPN customer gateway instance id.

## See Also

* [alicloud_vpn_customer_gateway](https://www.terraform.io/docs/providers/alicloud/r/vpn_customer_gateway.html) in the _Terraform Provider Documentation_