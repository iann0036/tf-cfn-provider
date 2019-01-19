# Terraform::VSphere::TagCategory

The `Terraform::VSphere::TagCategory` resource can be used to create and manage tag
categories, which determine how tags are grouped together and applied to
specific objects.

For more information about tags, click [here][ext-tags-general]. For more
information about tag categories specifically, click
[here][ext-tag-categories].

[ext-tags-general]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vcenterhost.doc/GUID-E8E854DD-AA97-4E0C-8419-CE84F93C4058.html
[ext-tag-categories]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vcenterhost.doc/GUID-BA3D1794-28F2-43F3-BCE9-3964CB207FB6.html

~> **NOTE:** Tagging support is unsupported on direct ESXi connections and
requires vCenter 6.0 or higher.

## Properties

`Name` - (Required) The name of the category.

`Cardinality` - (Required) The number of tags that can be assigned from this category to a single object at once. Can be one of `SINGLE` (object can only be assigned one tag in this category), to `MULTIPLE` (object can be assigned multiple tags in this category). Forces a new resource if changed.

`AssociableTypes` - (Required) A list object types that this category is valid to be assigned to. For a full list, click [here](#associable-object-types).

`Description` - (Optional) A description for the category.


## See Also

* [vsphere_tag_category](https://www.terraform.io/docs/providers/vsphere/r/tag_category.html) in the _Terraform Provider Documentation_