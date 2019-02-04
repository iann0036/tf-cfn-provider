# Terraform::VSphere::VirtualDisk

The `Terraform::VSphere::VirtualDisk` resource can be used to create virtual disks outside
of any given [`Terraform::VSphere::VirtualMachine`][docs-vsphere-virtual-machine]
resource. These disks can be attached to a virtual machine by creating a disk
block with the [`attach`][docs-vsphere-virtual-machine-disk-attach] parameter.

[docs-vsphere-virtual-machine]: /docs/providers/vsphere/r/virtual_machine.html
[docs-vsphere-virtual-machine-disk-attach]: /docs/providers/vsphere/r/virtual_machine.html#attach

## Properties

`VmdkPath` - (Required) The path, including filename, of the virtual disk to
be created.  This needs to end in `.vmdk`.

`Datastore` - (Required) The name of the datastore in which to create the
disk.

`Size` - (Required) Size of the disk (in GB).

`Datacenter` - (Optional) The name of the datacenter in which to create the
disk. Can be omitted when when ESXi or if there is only one datacenter in
your infrastructure.

`Type` - (Optional) The type of disk to create. Can be one of
`eagerZeroedThick`, `lazy`, or `thin`. Default: `eagerZeroedThick`. For
information on what each kind of disk provisioning policy means, click
[here][docs-vmware-vm-disk-provisioning].

`AdapterType` - (Optional) The adapter type for this virtual disk. Can be
one of `ide`, `lsiLogic`, or `busLogic`.  Default: `lsiLogic`.

`CreateDirectories` - (Optional) Tells the resource to create any
directories that are a part of the `VmdkPath` parameter if they are missing.
Default: `false`.


## See Also

* [vsphere_virtual_disk](https://www.terraform.io/docs/providers/vsphere/r/virtual_disk.html) in the _Terraform Provider Documentation_