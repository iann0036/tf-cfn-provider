# Terraform::VSphere::Tag

The `Terraform::VSphere::Tag` resource can be used to create and manage tags, which allow
you to attach metadata to objects in the vSphere inventory to make these
objects more sortable and searchable.

For more information about tags, click [here][ext-tags-general].

[ext-tags-general]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vcenterhost.doc/GUID-E8E854DD-AA97-4E0C-8419-CE84F93C4058.html

~> **NOTE:** Tagging support is unsupported on direct ESXi connections and
requires vCenter 6.0 or higher.

## Properties

`Name` - (Required) The display name of the tag. The name must be unique within its category.

`CategoryId` - (Required) The unique identifier of the parent category in which this tag will be created. Forces a new resource if changed.

`Description` - (Optional) A description for the tag.


## See Also

* [vsphere_tag](https://www.terraform.io/docs/providers/vsphere/r/tag.html) in the _Terraform Provider Documentation_