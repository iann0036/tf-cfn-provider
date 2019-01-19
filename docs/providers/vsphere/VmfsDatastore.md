# Terraform::VSphere::VmfsDatastore

The `Terraform::VSphere::VmfsDatastore` resource can be used to create and manage VMFS
datastores on an ESXi host or a set of hosts. The resource supports using any
SCSI device that can generally be used in a datastore, such as local disks, or
disks presented to a host or multiple hosts over Fibre Channel or iSCSI.
Devices can be specified manually, or discovered using the
[`Terraform::VSphere::VmfsDisks`][data-source-vmfs-disks] data source.

[data-source-vmfs-disks]: /docs/providers/vsphere/d/vmfs_disks.html

## Properties

`Name` - (Required) The name of the datastore. Forces a new resource if changed.

`HostSystemId` - (Required) The [managed object ID][docs-about-morefs] of the host to set the datastore up on. Note that this is not necessarily the only host that the datastore will be set up on - see [here](#auto-mounting-of-datastores-within-vcenter) for more info. Forces a new resource if changed.

`Disks` - (Required) The disks to use with the datastore.

`Folder` - (Optional) The relative path to a folder to put this datastore in. This is a path relative to the datacenter you are deploying the datastore to. Example: for the `dc1` datacenter, and a provided `Folder` of `foo/bar`, Terraform will place a datastore named `terraform-test` in a datastore folder located at `/dc1/datastore/foo/bar`, with the final inventory path being `/dc1/datastore/foo/bar/terraform-test`. Conflicts with `DatastoreClusterId`.

`DatastoreClusterId` - (Optional) The [managed object ID][docs-about-morefs] of a datastore cluster to put this datastore in. Conflicts with `Folder`.

`Tags` - (Optional) The IDs of any tags to attach to this resource. See [here][docs-applying-tags] for a reference on how to apply tags.


## See Also

* [vsphere_vmfs_datastore](https://www.terraform.io/docs/providers/vsphere/r/vmfs_datastore.html) in the _Terraform Provider Documentation_