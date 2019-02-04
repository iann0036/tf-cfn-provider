# Terraform::Chef::Role

A [role](http://docs.chef.io/roles.html) is a set of standard configuration
that can apply across multiple nodes that perform the same function.

## Properties

`Name` - (Required) The unique name to assign to the role.

`Description` - (Optional) A human-friendly description of the role.
If not set, a placeholder of "Managed by Terraform" will be set.

`DefaultAttributesJson` - (Optional) String containing a JSON-serialized
object containing the default attributes for the role.

`OverrideAttributesJson` - (Optional) String containing a JSON-serialized
object containing the override attributes for the role.

`RunList` - (Optional) List of strings to set as the
[run list](https://docs.chef.io/run_lists.html) for any nodes that belong
to this role.


## See Also

* [chef_role](https://www.terraform.io/docs/providers/chef/r/role.html) in the _Terraform Provider Documentation_