# Terraform::Chef::DataBag

A [data bag](http://docs.chef.io/data_bags.html) is a collection of
configuration objects that are stored as JSON in Chef Server and can be
retrieved and used in Chef recipes.

This resource creates the data bag itself. Inside each data bag is a collection
of items which can be created using the ``chef_data_bag_item`` resource.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`ApiUri` - The URI representing this data bag in the Chef server API.

## See Also

* [chef_data_bag](https://www.terraform.io/docs/providers/chef/r/data_bag.html) in the _Terraform Provider Documentation_