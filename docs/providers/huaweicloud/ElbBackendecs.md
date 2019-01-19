# Terraform::HuaweiCloud::ElbBackendecs

Manages an elastic loadbalancer backendecs resource within huawei cloud.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`ListenerId` - See Argument Reference above.

`ServerId` - See Argument Reference above.

`PrivateAddress` - See Argument Reference above.

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