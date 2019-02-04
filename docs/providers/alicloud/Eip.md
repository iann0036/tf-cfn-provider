# Terraform::Alicloud::Eip

Provides an elastic IP resource.

-> **NOTE:** The resource only support to create `PayByTraffic` elastic IP for international account. Otherwise, you will happened error `COMMODITY.INVALID_COMPONENT`.
Your account is international if you can use it to login in [International Web Console](https://account.alibabacloud.com/login/login.htm).

-> **NOTE:** From version 1.10.1, this resource supports creating "PrePaid" EIP. In addition, it supports setting EIP name and description.

## Properties

`Name` - (Optional) The name of the EIP instance. This name can have a string of 2 to 128 characters, must contain only alphanumeric characters or hyphens, such as "-",".","_", and must not begin or end with a hyphen, and must not begin with http:// or https://.

`Description` - (Optional) Description of the EIP instance, This description can have a string of 2 to 256 characters, It cannot begin with http:// or https://. Default value is null.

`Bandwidth` - (Optional) Maximum bandwidth to the elastic public network, measured in Mbps (Mega bit per second). If this value is not specified, then automatically sets it to 5 Mbps.

`InternetChargeType` - (Optional, ForceNew) Internet charge type of the EIP, Valid values are `PayByBandwidth`, `PayByTraffic`. Default to `PayByBandwidth`. From version `1.7.1`, default to `PayByTraffic`.

`InstanceChargeType` - (Optional, ForceNew) Elastic IP instance charge type. Valid values are "PrePaid" and "PostPaid". Default to "PostPaid".

`Period` - (Optional, ForceNew) The duration that you will buy the resource, in month. It is valid when `InstanceChargeType` is `PrePaid`.
Default to 1. Valid values: [1-9, 12, 24, 36]. At present, the provider does not support modify "period" and you can do that via web console.


## Return Values

### Fn::GetAtt

`Id` - The EIP ID.

`Bandwidth` - The elastic public network bandwidth.

`InternetChargeType` - The EIP internet charge type.

`Status` - The EIP current status.

`IpAddress` - The elastic ip address.

## See Also

* [alicloud_eip](https://www.terraform.io/docs/providers/alicloud/r/eip.html) in the _Terraform Provider Documentation_