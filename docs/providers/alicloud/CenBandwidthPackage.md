# Terraform::Alicloud::CenBandwidthPackage

Provides a CEN bandwidth package resource. The CEN bandwidth package is an abstracted object that includes an interconnection bandwidth and interconnection areas. To buy a bandwidth package, you must specify the areas to connect. An area consists of one or more Alibaba Cloud regions. The areas in CEN include Mainland China, Asia Pacific, North America, and Europe.

For information about CEN and how to use it, see [Manage bandwidth packages](https://www.alibabacloud.com/help/doc-detail/65982.htm).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the bandwidth package.

`ExpiredTime` - The time of the bandwidth package to expire.

`Status` - The status of the bandwidth, including "InUse" and "Idle".

## See Also

* [alicloud_cen_bandwidth_package](https://www.terraform.io/docs/providers/alicloud/r/cen_bandwidth_package.html) in the _Terraform Provider Documentation_