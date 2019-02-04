# Terraform::OpenTelekomCloud::ElbBackend

Manages an elastic loadbalancer backend resource within OpentelekomCloud.

## Properties

`ListenerId` - (Required) Specifies the listener ID. Changing this creates a new
elb backend.

`ServerId` - (Required) Specifies the backend member ID. Changing this creates a
new elb backend.

`Address` - (Required) Specifies the private IP address of the backend member.
Changing this creates a new elb backend.


## Return Values

### Fn::GetAtt

`ListenerId` - See Properties above.

`ServerId` - See Properties above.

`Address` - See Properties above.

`ServerAddress` - Specifies the floating IP address assigned to the backend member.

`Id` - Specifies the backend member ID.

`Status` - Specifies the backend ECS status. The value is ACTIVE, PENDING,.

`HealthStatus` - Specifies the health check status. The value is NORMAL,.

`UpdateTime` - Specifies the time when information about the backend member.

`CreateTime` - Specifies the time when the backend member was created.

`ServerName` - Specifies the backend member name.

`Listeners` - Specifies the listener to which the backend member belongs.

## See Also

* [opentelekomcloud_elb_backend](https://www.terraform.io/docs/providers/opentelekomcloud/r/elb_backend.html) in the _Terraform Provider Documentation_