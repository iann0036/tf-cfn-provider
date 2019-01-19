# Terraform::Chef::DataBagItem

A [data bag](http://docs.chef.io/data_bags.html) is a collection of
configuration objects that are stored as JSON in Chef Server and can be
retrieved and used in Chef recipes.

This resource creates objects within an existing data bag. To create the
data bag itself, use the ``Terraform::Chef::DataBag`` resource.

## Properties

`DataBagName` - (Required) The name of the data bag into which this item will be placed.

`ContentJson` - (Required) A string containing a JSON object that will be the content of the item. Must at minimum contain a property called "id" that is unique within the data bag, which will become the identifier of the created item.


## Return Values

### Fn::GetAtt

`Id` - The value of the "id" property in the ``ContentJson`` JSON object,.

## See Also

* [chef_data_bag_item](https://www.terraform.io/docs/providers/chef/r/data_bag_item.html) in the _Terraform Provider Documentation_