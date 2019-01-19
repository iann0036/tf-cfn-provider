# Terraform::VSphere::VirtualDisk

The `vsphere_virtual_disk` resource can be used to create virtual disks outside
of any given [`vsphere_virtual_machine`][docs-vsphere-virtual-machine]
resource. These disks can be attached to a virtual machine by creating a disk
block with the [`attach`][docs-vsphere-virtual-machine-disk-attach] parameter.

[docs-vsphere-virtual-machine]: /docs/providers/vsphere/r/virtual_machine.html
[docs-vsphere-virtual-machine-disk-attach]: /docs/providers/vsphere/r/virtual_machine.html#attach

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [vsphere_virtual_disk](https://www.terraform.io/docs/providers/vsphere/r/virtual_disk.html) in the _Terraform Provider Documentation_