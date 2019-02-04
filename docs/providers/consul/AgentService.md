# Terraform::Consul::AgentService

!> The `Terraform::Consul::AgentService` resource has been deprecated in version 2.0.0 of the provider
and will be removed in a future release. Please read the [upgrade guide](/docs/providers/consul/upgrading.html#deprecation-of-consul_agent_service)
for more information.

Provides access to the agent service data in Consul. This can be used to
define a service associated with a particular agent. Currently, defining
health checks for an agent service is not supported.

## Properties

`Address` - (Optional) The address of the service. Defaults to the
address of the agent.

`Name` - (Required) The name of the service.

`Port` - (Optional) The port of the service.

`Tags` - (Optional) A list of values that are opaque to Consul,
but can be used to distinguish between services or nodes.


## Return Values

### Fn::GetAtt

`Address` - The address of the service.

`Id` - The ID of the service, defaults to the value of `Name`.

`Name` - The name of the service.

`Port` - The port of the service.

`Tags` - The tags of the service.

## See Also

* [consul_agent_service](https://www.terraform.io/docs/providers/consul/r/agent_service.html) in the _Terraform Provider Documentation_