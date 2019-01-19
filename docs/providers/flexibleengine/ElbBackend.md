# Terraform::FlexibleEngine::ElbBackend

Manages an elastic loadbalancer backend resource within FlexibleEngine.

## Properties

`ListenerId` - (Required) Specifies the listener ID.

`ServerId` - (Required) Specifies the backend member ID.

`Address` - (Required) Specifies the private IP address of the backend member.


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

* [flexibleengine_elb_backend](https://www.terraform.io/docs/providers/flexibleengine/r/elb_backend.html) in the _Terraform Provider Documentation_