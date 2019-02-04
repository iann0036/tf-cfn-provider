# Terraform::Chef::Node

A [node](http://docs.chef.io/nodes.html) is a computer whose
configuration is managed by Chef.

Although this resource allows a node to be registered, it does not actually
configure the computer in question to interact with Chef. In most cases it
is better to use [the `chef` provisioner](/docs/provisioners/chef.html) to
configure the Chef client on a computer and have it register itself with the
Chef server.

## Properties

`Name` - (Required) The unique name to assign to the node.

`EnvironmentName` - (Optional) the nodes environment name (default: _default).

`AutomaticAttributesJson` - (Optional) String containing a JSON-serialized
object containing the automatic attributes for the node.

`NormalAttributesJson` - (Optional) String containing a JSON-serialized
object containing the normal attributes for the node.

`DefaultAttributesJson` - (Optional) String containing a JSON-serialized
object containing the default attributes for the node.

`OverrideAttributesJson` - (Optional) String containing a JSON-serialized
object containing the override attributes for the node.

`RunList` - (Optional) List of strings to set as the
[run list](https://docs.chef.io/run_lists.html) for the node.


## See Also

* [chef_node](https://www.terraform.io/docs/providers/chef/r/node.html) in the _Terraform Provider Documentation_