# Terraform::Chef::Node

A [node](http://docs.chef.io/nodes.html) is a computer whose
configuration is managed by Chef.

Although this resource allows a node to be registered, it does not actually
configure the computer in question to interact with Chef. In most cases it
is better to use [the `chef` provisioner](/docs/provisioners/chef.html) to
configure the Chef client on a computer and have it register itself with the
Chef server.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [chef_node](https://www.terraform.io/docs/providers/chef/r/node.html) in the _Terraform Provider Documentation_