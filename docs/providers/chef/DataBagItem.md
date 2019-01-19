# Terraform::Chef::DataBagItem

A [data bag](http://docs.chef.io/data_bags.html) is a collection of
configuration objects that are stored as JSON in Chef Server and can be
retrieved and used in Chef recipes.

This resource creates objects within an existing data bag. To create the
data bag itself, use the ``chef_data_bag`` resource.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The value of the "id" property in the ``content_json`` JSON object,.

## See Also

* [chef_data_bag_item](https://www.terraform.io/docs/providers/chef/r/data_bag_item.html) in the _Terraform Provider Documentation_