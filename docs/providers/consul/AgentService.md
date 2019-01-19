# Terraform::Consul::AgentService

!> The `consul_agent_service` resource has been deprecated in version 2.0.0 of the provider
and will be removed in a future release. Please read the [upgrade guide](/docs/providers/consul/upgrading.html#deprecation-of-consul_agent_service)
for more information.

Provides access to the agent service data in Consul. This can be used to
define a service associated with a particular agent. Currently, defining
health checks for an agent service is not supported.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Address` - The address of the service.

`Id` - The ID of the service, defaults to the value of `name`.

`Name` - The name of the service.

`Port` - The port of the service.

`Tags` - The tags of the service.

## See Also

* [consul_agent_service](https://www.terraform.io/docs/providers/consul/r/agent_service.html) in the _Terraform Provider Documentation_