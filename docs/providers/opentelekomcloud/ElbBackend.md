# Terraform::OpenTelekomCloud::ElbBackend

Manages an elastic loadbalancer backend resource within OpentelekomCloud.

## Properties

TBC

## Return Values

### Fn::GetAtt

`ListenerId` - See Argument Reference above.

`ServerId` - See Argument Reference above.

`Address` - See Argument Reference above.

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