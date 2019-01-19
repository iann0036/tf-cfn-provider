# Terraform::UCloud::LbAttachment

Provides a Load Balancer Attachment resource for attaching Load Balancer to UHost Instance, etc.

## Properties

`LoadBalancerId` - (Required) The ID of load balancer instance.

`ListenerId` - (Required) The ID of listener servers.

`ResourceType` - (Required) **Deprecated**, attribute `ResourceType` is deprecated for optimizing parameters.

`ResourceId` - (Required) The ID of backend servers.

`Port` - (Optional) Port opened on the backend server to receive requests, range: 1-65535, (Default: `80`).


## Return Values

### Fn::GetAtt

`PrivateIp` - The private ip address for backend servers.

`Status` - The status of backend servers. Possible values are: `normalRunning`, `exceptionRunning`.

## See Also

* [ucloud_lb_attachment](https://www.terraform.io/docs/providers/ucloud/r/lb_attachment.html) in the _Terraform Provider Documentation_