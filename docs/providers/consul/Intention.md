# Terraform::Consul::Intention

[Intentions](https://www.consul.io/docs/connect/intentions.html) are used to define
rules for which services may connect to one another when using [Consul Connect](https://www.consul.io/docs/connect/index.html).

It is appropriate to either reference existing services or specify non-existent services
that will be created in the future when creating intentions. This resource can be used
in conjunction with the `Terraform::Consul::Service` datasource when referencing services
registered on nodes that have a running Consul agent.

## Properties

`SourceName` - (Required, string) The name of the source service for the intention. This service does not have to exist.

`DestinationName` - (Required, string) The name of the destination service for the intention. This service does not have to exist.

`Action` - (Required, string) The intention action. Must be one of `allow` or `deny`.

`Meta` - (Optional, map) Key/value pairs that are opaque to Consul and are associated with the intention.

`Description` - (Optional, string) Optional description that can be used by Consul tooling, but is not used internally.

`Datacenter` - (Optional) The datacenter to use. This overrides the datacenter in the provider setup and the agent's default datacenter.


## Return Values

### Fn::GetAtt

`Id` - The ID of the intention.

`SourceName` - The source for the intention.

`DestinationName` - The destination for the intention.

`Description` - A description of the intention.

`Meta` - Key/value pairs associated with the intention.

## See Also

* [consul_intention](https://www.terraform.io/docs/providers/consul/r/intention.html) in the _Terraform Provider Documentation_