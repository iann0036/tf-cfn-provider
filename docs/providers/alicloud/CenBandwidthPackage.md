# Terraform::Alicloud::CenBandwidthPackage

Provides a CEN bandwidth package resource. The CEN bandwidth package is an abstracted object that includes an interconnection bandwidth and interconnection areas. To buy a bandwidth package, you must specify the areas to connect. An area consists of one or more Alibaba Cloud regions. The areas in CEN include Mainland China, Asia Pacific, North America, and Europe.

For information about CEN and how to use it, see [Manage bandwidth packages](https://www.alibabacloud.com/help/doc-detail/65982.htm).

## Properties

`Bandwidth` - (Required) The bandwidth in Mbps of the bandwidth package. Cannot be less than 1Mbps.

`GeographicRegionIds` - (Required) List of the two areas to connect. Valid value: China | North-America | Asia-Pacific | Europe | Middle-East.

`Name` - (Optional) The name of the bandwidth package. Defaults to null.

`Description` - (Optional) The description of the bandwidth package. Default to null.

`ChargeType` - (Optional) The billing method. Valid value: PostPaid | PrePaid. Default to PostPaid. If set to PrePaid, the bandwidth package can't be deleted before expired time.

`Period` - (Optional) The purchase period in month. Valid value: 1, 2, 3, 6, 12. Default to 1.


## Return Values

### Fn::GetAtt

`Id` - The ID of the bandwidth package.

`ExpiredTime` - The time of the bandwidth package to expire.

`Status` - The status of the bandwidth, including "InUse" and "Idle".

## See Also

* [alicloud_cen_bandwidth_package](https://www.terraform.io/docs/providers/alicloud/r/cen_bandwidth_package.html) in the _Terraform Provider Documentation_