# Terraform::Consul::Intention

[Intentions](https://www.consul.io/docs/connect/intentions.html) are used to define
rules for which services may connect to one another when using [Consul Connect](https://www.consul.io/docs/connect/index.html).

It is appropriate to either reference existing services or specify non-existent services
that will be created in the future when creating intentions. This resource can be used
in conjunction with the `consul_service` datasource when referencing services
registered on nodes that have a running Consul agent.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the intention.

`SourceName` - The source for the intention.

`DestinationName` - The destination for the intention.

`Description` - A description of the intention.

`Meta` - Key/value pairs associated with the intention.

## See Also

* [consul_intention](https://www.terraform.io/docs/providers/consul/r/intention.html) in the _Terraform Provider Documentation_