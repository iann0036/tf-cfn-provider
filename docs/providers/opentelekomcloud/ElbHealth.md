# Terraform::OpenTelekomCloud::ElbHealth

Manages an elastic loadbalancer health resource within OpentelekomCloud.

## Properties

`Region` - (Optional) The region in which to create the elb health. If
omitted, the `Region` argument of the provider is used. Changing this
creates a new elb health.

`ListenerId` - (Required) Specifies the ID of the listener to which the health
check task belongs. Changing this creates a new elb health.

`HealthcheckProtocol` - (Optional) Specifies the protocol used for the health
check. The value can be HTTP or TCP (case-insensitive).

`HealthcheckUri` - (Optional) Specifies the URI for health check. This parameter
is valid when healthcheck_ protocol is HTTP. The value is a string of 1 to 80
characters that must start with a slash (/) and can only contain letters, digits,
and special characters, such as -/.%?#&.

`HealthcheckConnectPort` - (Optional) Specifies the port used for the health
check. The value ranges from 1 to 65535.

`HealthyThreshold` - (Optional) Specifies the threshold at which the health
check result is success, that is, the number of consecutive successful health
checks when the health check result of the backend server changes from fail
to success. The value ranges from 1 to 10.

`UnhealthyThreshold` - (Optional) Specifies the threshold at which the health
check result is fail, that is, the number of consecutive failed health checks
when the health check result of the backend server changes from success to fail.
The value ranges from 1 to 10.

`HealthcheckTimeout` - (Optional) Specifies the maximum timeout duration
(s) for the health check. The value ranges from 1 to 50.

`HealthcheckInterval` - (Optional) Specifies the maximum interval (s) for
health check. The value ranges from 1 to 5.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`ListenerId` - See Properties above.

`HealthcheckProtocol` - See Properties above.

`HealthcheckUri` - See Properties above.

`HealthcheckConnectPort` - See Properties above.

`HealthyThreshold` - See Properties above.

`UnhealthyThreshold` - See Properties above.

`HealthcheckTimeout` - See Properties above.

`HealthcheckInterval` - See Properties above.

`Id` - Specifies the health check task ID.

## See Also

* [opentelekomcloud_elb_health](https://www.terraform.io/docs/providers/opentelekomcloud/r/elb_health.html) in the _Terraform Provider Documentation_