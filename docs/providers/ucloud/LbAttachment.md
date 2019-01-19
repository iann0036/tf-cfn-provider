# Terraform::UCloud::LbAttachment

Provides a Load Balancer Attachment resource for attaching Load Balancer to UHost Instance, etc.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`PrivateIp` - The private ip address for backend servers.

`Status` - The status of backend servers. Possible values are: `normalRunning`, `exceptionRunning`.

## See Also

* [ucloud_lb_attachment](https://www.terraform.io/docs/providers/ucloud/r/lb_attachment.html) in the _Terraform Provider Documentation_