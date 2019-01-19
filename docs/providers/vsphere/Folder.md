# Terraform::VSphere::Folder

The `Terraform::VSphere::Folder` resource can be used to manage vSphere inventory folders.
The resource supports creating folders of the 5 major types - datacenter
folders, host and cluster folders, virtual machine folders, datastore folders,
and network folders.

Paths are always relative to the specific type of folder you are creating.
Subfolders are discovered by parsing the relative path specified in `Path`, so
`foo/bar` will create a folder named `bar` in the parent folder `foo`, as long
as that folder exists.

## Properties

`Path` - (Required) The path of the folder to be created. This is relative to the root of the type of folder you are creating, and the supplied datacenter. For example, given a default datacenter of `default-dc`, a folder of type `vm` (denoting a virtual machine folder), and a supplied folder of `terraform-test-folder`, the resulting path would be `/default-dc/vm/terraform-test-folder`.

`Type` - (Required) The type of folder to create. Allowed options are `datacenter` for datacenter folders, `host` for host and cluster folders, `vm` for virtual machine folders, `datastore` for datastore folders, and `network` for network folders. Forces a new resource if changed.

`DatacenterId` - The ID of the datacenter the folder will be created in. Required for all folder types except for datacenter folders. Forces a new resource if changed.

`Tags` - (Optional) The IDs of any tags to attach to this resource. See [here][docs-applying-tags] for a reference on how to apply tags.

`CustomAttributes` - (Optional) Map of custom attribute ids to attribute value strings to set for folder. See [here][docs-setting-custom-attributes] for a reference on how to set values for custom attributes.


## See Also

* [vsphere_folder](https://www.terraform.io/docs/providers/vsphere/r/folder.html) in the _Terraform Provider Documentation_