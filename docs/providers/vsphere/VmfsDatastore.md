# Terraform::VSphere::VmfsDatastore

The `vsphere_vmfs_datastore` resource can be used to create and manage VMFS
datastores on an ESXi host or a set of hosts. The resource supports using any
SCSI device that can generally be used in a datastore, such as local disks, or
disks presented to a host or multiple hosts over Fibre Channel or iSCSI.
Devices can be specified manually, or discovered using the
[`vsphere_vmfs_disks`][data-source-vmfs-disks] data source.

[data-source-vmfs-disks]: /docs/providers/vsphere/d/vmfs_disks.html

## Properties

TBC

## See Also

* [vsphere_vmfs_datastore](https://www.terraform.io/docs/providers/vsphere/r/vmfs_datastore.html) in the _Terraform Provider Documentation_