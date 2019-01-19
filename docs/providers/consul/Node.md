# Terraform::Consul::Node

Provides access to Node data in Consul. This can be used to define a
node. Currently, defining health checks is not supported.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Address` - The address of the service.

`Name` - The name of the service.

`Meta` - (Optional, map) Key/value pairs that are associated with the node.

## See Also

* [consul_node](https://www.terraform.io/docs/providers/consul/r/node.html) in the _Terraform Provider Documentation_