# Terraform::TencentCloud::AlbServerAttachment

Provides Load Balancer server attachment resource.

~> **NOTE:** Currently only support existing `loadbalancer_id` `listener_id` `location_id` and Application layer 7 load balancer

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`LoadbalancerId` - loadbalancer ID.

`ListenerId` - listener ID.

`LocationId` - location ID (only support for layer 7 loadbalancer).

`ProtocolType` - http or tcp.

## See Also

* [tencentcloud_alb_server_attachment](https://www.terraform.io/docs/providers/tencentcloud/r/alb_server_attachment.html) in the _Terraform Provider Documentation_