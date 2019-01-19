# Terraform::TencentCloud::AlbServerAttachment

Provides Load Balancer server attachment resource.

~> **NOTE:** Currently only support existing `LoadbalancerId` `ListenerId` `LocationId` and Application layer 7 load balancer

## Properties

`LoadbalancerId` - (Required, Forces new resource) loadbalancer ID.

`ListenerId` - (Required, Forces new resource) listener ID.

`LocationId` - (Optional) location ID only support for layer 7 loadbalancer.

`Backends` - (Required) list of backend server. Valid value range [1-100].


## Return Values

### Fn::GetAtt

`LoadbalancerId` - loadbalancer ID.

`ListenerId` - listener ID.

`LocationId` - location ID (only support for layer 7 loadbalancer).

`ProtocolType` - http or tcp.

## See Also

* [tencentcloud_alb_server_attachment](https://www.terraform.io/docs/providers/tencentcloud/r/alb_server_attachment.html) in the _Terraform Provider Documentation_