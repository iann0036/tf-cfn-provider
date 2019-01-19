# Terraform::Consul::CatalogEntry

!> The `consul_catalog_entry` resource has been deprecated in version 2.0.0 of the provider
and will be removed in a future release. Please read the [upgrade guide](/docs/providers/consul/upgrading.html#deprecation-of-consul_catalog_entry)
for more information.

Registers a node or service with the [Consul Catalog](https://www.consul.io/docs/agent/http/catalog.html#catalog_register).
Currently, defining health checks is not supported.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Address` - The address of the service.

`Node` - The ID of the service, defaults to the value of `name`.

## See Also

* [consul_catalog_entry](https://www.terraform.io/docs/providers/consul/r/catalog_entry.html) in the _Terraform Provider Documentation_