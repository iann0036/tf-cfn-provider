# Terraform::Consul::Service

A high-level resource for creating a Service in Consul in the Consul catalog. This
is appropriate for registering [external services](https://www.consul.io/docs/guides/external.html) and
can be used to create services addressable by Consul that cannot be registered
with a [local agent](https://www.consul.io/docs/agent/basics.html).

If the Consul agent is running on the node where this service is registered, it is
not recommended to use this resource.

## Properties

`Name` - (Required, string) The name of the service.

`Node` - (Required, string) The name of the node the to register the service on.

`Address` - (Optional, string) The address of the service. Defaults to the address of the node.

`Port` - (Optional, int) The port of the service.

`Tags` - (Optional, set of strings) A list of values that are opaque to Consul, but can be used to distinguish between services or nodes.

`Datacenter` - (Optional) The datacenter to use. This overrides the datacenter in the provider setup and the agent's default datacenter.


## Return Values

### Fn::GetAtt

`ServiceId` - The ID of the service.

`Address` - The address of the service.

`Node` - The node the service is registered on.

`Name` - The name of the service.

`Port` - The port of the service.

`Tags` - The tags of the service.

## See Also

* [consul_service](https://www.terraform.io/docs/providers/consul/r/service.html) in the _Terraform Provider Documentation_