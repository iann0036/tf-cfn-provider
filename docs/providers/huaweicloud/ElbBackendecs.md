# Terraform::HuaweiCloud::ElbBackendecs

Manages an elastic loadbalancer backendecs resource within huawei cloud.

## Properties

`ListenerId` - (Required) Specifies the listener ID.

`ServerId` - (Required) Specifies the backend member ID.

`PrivateAddress` - (Required) Specifies the private IP address of the backend member.


## Return Values

### Fn::GetAtt

`ListenerId` - See Properties above.

`ServerId` - See Properties above.

`PrivateAddress` - See Properties above.

`PublicAddress` - Specifies the floating IP address assigned to the backend member.

`Id` - Specifies the backend member ID.

`Status` - Specifies the backend ECS status. The value is ACTIVE, PENDING,.

`HealthStatus` - Specifies the health check status. The value is NORMAL,.

`UpdateTime` - Specifies the time when information about the backend member.

`CreateTime` - Specifies the time when the backend member was created.

`ServerName` - Specifies the backend member name.

`Listeners` - Specifies the listener to which the backend member belongs.

## See Also

* [huaweicloud_elb_backendecs](https://www.terraform.io/docs/providers/huaweicloud/r/elb_backendecs.html) in the _Terraform Provider Documentation_