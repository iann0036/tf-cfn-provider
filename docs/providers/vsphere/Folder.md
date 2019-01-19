# Terraform::VSphere::Folder

The `vsphere_folder` resource can be used to manage vSphere inventory folders.
The resource supports creating folders of the 5 major types - datacenter
folders, host and cluster folders, virtual machine folders, datastore folders,
and network folders.

Paths are always relative to the specific type of folder you are creating.
Subfolders are discovered by parsing the relative path specified in `path`, so
`foo/bar` will create a folder named `bar` in the parent folder `foo`, as long
as that folder exists.

## Properties

TBC

## See Also

* [vsphere_folder](https://www.terraform.io/docs/providers/vsphere/r/folder.html) in the _Terraform Provider Documentation_