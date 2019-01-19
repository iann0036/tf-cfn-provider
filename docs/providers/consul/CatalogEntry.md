# Terraform::Consul::CatalogEntry

!> The `Terraform::Consul::CatalogEntry` resource has been deprecated in version 2.0.0 of the provider
and will be removed in a future release. Please read the [upgrade guide](/docs/providers/consul/upgrading.html#deprecation-of-consul_catalog_entry)
for more information.

Registers a node or service with the [Consul Catalog](https://www.consul.io/docs/agent/http/catalog.html#catalog_register).
Currently, defining health checks is not supported.

## Properties

`Node` - (Required) The name of the node being added to, or referenced in the catalog.

`Service` - (Optional) A service to optionally associated with the node. Supported values are documented below.

`Datacenter` - (Optional) The datacenter to use. This overrides the datacenter in the provider setup and the agent's default datacenter.

`Token` - (Optional) ACL token.

### Service Properties

`Address` - (Optional) The address of the service. Defaults to the node address.

`Id` - (Optional) The ID of the service. Defaults to the `Name`.

`Name` - (Required) The name of the service.

`Port` - (Optional) The port of the service.

`Tags` - (Optional) A list of values that are opaque to Consul, but can be used to distinguish between services or nodes.


## Return Values

### Fn::GetAtt

`Address` - The address of the service.

`Node` - The ID of the service, defaults to the value of `Name`.

## See Also

* [consul_catalog_entry](https://www.terraform.io/docs/providers/consul/r/catalog_entry.html) in the _Terraform Provider Documentation_