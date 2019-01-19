# Terraform::VSphere::VirtualMachineSnapshot

The `Terraform::VSphere::VirtualMachineSnapshot` resource can be used to manage snapshots
for a virtual machine.

For more information on managing snapshots and how they work in VMware, see
[here][ext-vm-snapshot-management].

[ext-vm-snapshot-management]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vm_admin.doc/GUID-CA948C69-7F58-4519-AEB1-739545EA94E5.html

~> **NOTE:** A snapshot in VMware differs from traditional disk snapshots, and
can contain the actual running state of the virtual machine, data for all disks
that have not been set to be independent from the snapshot (including ones that
have been attached via the [attach][docs-vsphere-virtual-machine-disk-attach]
parameter to the `Terraform::VSphere::VirtualMachine` `disk` block), and even the
configuration of the virtual machine at the time of the snapshot. Virtual
machine, disk activity, and configuration changes post-snapshot are not
included in the original state. Use this resource with care! Neither VMware nor
HashiCorp recommends retaining snapshots for a extended period of time and does
NOT recommend using them as as backup feature. For more information on the
limitation of virtual machine snapshots, see [here][ext-vm-snap-limitations].

[docs-vsphere-virtual-machine-disk-attach]: /docs/providers/vsphere/r/virtual_machine.html#attach
[ext-vm-snap-limitations]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vm_admin.doc/GUID-53F65726-A23B-4CF0-A7D5-48E584B88613.html

## Properties

`VirtualMachineUuid` - (Required) The virtual machine UUID.

`SnapshotName` - (Required) The name of the snapshot.

`Description` - (Required) A description for the snapshot.

`Memory` - (Required) If set to `true`, a dump of the internal state of the virtual machine is included in the snapshot.

`Quiesce` - (Required) If set to `true`, and the virtual machine is powered on when the snapshot is taken, VMware Tools is used to quiesce the file system in the virtual machine.

`RemoveChildren` - (Optional) If set to `true`, the entire snapshot subtree is removed when this resource is destroyed.

`Consolidate` - (Optional) If set to `true`, the delta disks involved in this snapshot will be consolidated into the parent when this resource is destroyed.


## See Also

* [vsphere_virtual_machine_snapshot](https://www.terraform.io/docs/providers/vsphere/r/virtual_machine_snapshot.html) in the _Terraform Provider Documentation_