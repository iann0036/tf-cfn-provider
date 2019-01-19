# Terraform::Chef::Environment

An [environment](http://docs.chef.io/environments.html) is a container for
Chef nodes that share a set of attribute values and may have a set of version
constraints for which cookbook versions may be used on its nodes.

## Properties

`Name` - (Required) The unique name to assign to the environment. This name will be used when nodes are created within the environment.

`Description` - (Optional) A human-friendly description of the environment. If not set, a placeholder of "Managed by Terraform" will be set.

`DefaultAttributesJson` - (Optional) String containing a JSON-serialized object containing the default attributes for the environment.

`OverrideAttributesJson` - (Optional) String containing a JSON-serialized object containing the override attributes for the environment.

`CookbookConstraints` - (Optional) Mapping of cookbook names to cookbook version constraints that should apply for this environment.


## See Also

* [chef_environment](https://www.terraform.io/docs/providers/chef/r/environment.html) in the _Terraform Provider Documentation_