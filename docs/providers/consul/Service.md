# Terraform::Consul::Service

A high-level resource for creating a Service in Consul in the Consul catalog. This
is appropriate for registering [external services](https://www.consul.io/docs/guides/external.html) and
can be used to create services addressable by Consul that cannot be registered
with a [local agent](https://www.consul.io/docs/agent/basics.html).

If the Consul agent is running on the node where this service is registered, it is
not recommended to use this resource.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`ServiceId` - The ID of the service.

`Address` - The address of the service.

`Node` - The node the service is registered on.

`Name` - The name of the service.

`Port` - The port of the service.

`Tags` - The tags of the service.

## See Also

* [consul_service](https://www.terraform.io/docs/providers/consul/r/service.html) in the _Terraform Provider Documentation_