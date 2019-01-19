# Terraform::Alicloud::Snat

Provides a snat resource.

## Properties

`SnatTableId` - (Required, Forces new resource) The value can get from `Terraform::Alicloud::NatGateway` Attributes "snat_table_ids".

`SourceVswitchId` - (Required, Forces new resource) The vswitch ID.

`SnatIp` - (Required) The SNAT ip address, the ip must along bandwidth package public ip which `Terraform::Alicloud::NatGateway` argument `bandwidthPackages`.


## See Also

* [alicloud_snat](https://www.terraform.io/docs/providers/alicloud/r/snat.html) in the _Terraform Provider Documentation_