# Terraform::OPC::ComputeStorageVolume

The ``opc_compute_storage_volume`` resource creates and manages a storage volume in an Oracle Cloud Infrastructure Compute Classic identity domain.

~> **Caution:** The ``opc_compute_storage_volume`` resource can completely delete your storage volume just as easily as it can create it. To avoid costly accidents, consider setting [``prevent_destroy``](/docs/configuration/resources.html#prevent_destroy) on your storage volume resources as an extra safety measure.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Hypervisor` - The hypervisor that this volume is compatible with.

`MachineImage` - Name of the Machine Image - available if the volume is a bootable storage volume.

`Managed` - Is this a Managed Volume?.

`Platform` - The OS platform this volume is compatible with.

`Readonly` - Can this Volume be attached as readonly?.

`Status` - The current state of the storage volume.

`StoragePool` - The storage pool from which this volume is allocated.

`Uri` - Unique Resource Identifier of the Storage Volume.

## See Also

* [opc_compute_storage_volume](https://www.terraform.io/docs/providers/opc/r/compute_storage_volume.html) in the _Terraform Provider Documentation_