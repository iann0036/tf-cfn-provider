# Terraform::VCD::Catalog

Provides a vCloud Director catalog resource. This can be used to create and delete a catalog.

Supported in provider *v2.0+*

## Properties

`Org` - (Optional) The name of organization to use, optional if defined at provider level. Useful when connected as sysadmin working across different organisations.

`Name` - (Required) Catalog name.

`Description` - (Optional) - Description of catalog.

`DeleteRecursive` - (Required) - When destroying use delete_recursive=True to remove the catalog and any objects it contains that are in a state that normally allows removal.


## See Also

* [vcd_catalog](https://www.terraform.io/docs/providers/vcd/r/catalog.html) in the _Terraform Provider Documentation_