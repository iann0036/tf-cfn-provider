# Terraform::Alicloud::CommonBandwidthPackage

Provides a common bandwidth package resource.

~> **NOTE:** Terraform will auto build common bandwidth package instance while it uses `Terraform::Alicloud::CommonBandwidthPackage` to build a common bandwidth package resource.

For information about common bandwidth package and how to use it, see [What is Common Bandwidth Package](https://www.alibabacloud.com/help/product/55092.htm).

For information about common bandwidth package billing methods, see [Common Bandwidth Package Billing Methods](https://www.alibabacloud.com/help/doc-detail/67459.html?spm=a2c5t.11065259.1996646101.searchclickresult.7ec93235Vfkwhy).

## Properties

`Bandwidth` - (Required) The bandwidth of the common bandwidth package, in Mbps.

`InternetChargeType` - (Optional, ForceNew) The billing method of the common bandwidth package. Valid values are "PayByBandwidth" and "PayBy95" and "PayByTraffic". "PayBy95" is pay by classic 95th percentile pricing. International Account doesn't supports "PayByBandwidth" and "PayBy95". Default to "PayByTraffic".

`Ratio` - (Optional) Ratio of the common bandwidth package. It is valid when `InternetChargeType` is `PayBy95`. Default to 100. Valid values: [10-100].

`Name` - (Optional) The name of the common bandwidth package.

`Description` - (Optional) The description of the common bandwidth package instance.


## Return Values

### Fn::GetAtt

`Id` - The ID of the common bandwidth package instance id.

## See Also

* [alicloud_common_bandwidth_package](https://www.terraform.io/docs/providers/alicloud/r/common_bandwidth_package.html) in the _Terraform Provider Documentation_