# Terraform::Alicloud::Forward

Provides a forward resource.

## Properties

`ForwardTableId` - (Required, Forces new resource) The value can get from `Terraform::Alicloud::NatGateway` Attributes "forward_table_ids".

`ExternalIp` - (Required, Forces new resource) The external ip address, the ip must along bandwidth package public ip which `Terraform::Alicloud::NatGateway` argument `bandwidthPackages`.

`ExternalPort` - (Required) The external port, valid value is 1~65535|any.

`IpProtocol` - (Required) The ip protocal, valid value is tcp|udp|any.

`InternalIp` - (Required) The internal ip, must a private ip.

`InternalPort` - (Required) The internal port, valid value is 1~65535|any.


## See Also

* [alicloud_forward](https://www.terraform.io/docs/providers/alicloud/r/forward.html) in the _Terraform Provider Documentation_