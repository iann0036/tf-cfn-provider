# Terraform::Alicloud::Eip

Provides an elastic IP resource.

-> **NOTE:** The resource only support to create `PayByTraffic` elastic IP for international account. Otherwise, you will happened error `COMMODITY.INVALID_COMPONENT`.
Your account is international if you can use it to login in [International Web Console](https://account.alibabacloud.com/login/login.htm).

-> **NOTE:** From version 1.10.1, this resource supports creating "PrePaid" EIP. In addition, it supports setting EIP name and description.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The EIP ID.

`Bandwidth` - The elastic public network bandwidth.

`InternetChargeType` - The EIP internet charge type.

`Status` - The EIP current status.

`IpAddress` - The elastic ip address.

## See Also

* [alicloud_eip](https://www.terraform.io/docs/providers/alicloud/r/eip.html) in the _Terraform Provider Documentation_