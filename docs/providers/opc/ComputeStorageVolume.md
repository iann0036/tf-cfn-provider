# Terraform::OPC::ComputeStorageVolume

The ``Terraform::OPC::ComputeStorageVolume`` resource creates and manages a storage volume in an Oracle Cloud Infrastructure Compute Classic identity domain.

~> **Caution:** The ``Terraform::OPC::ComputeStorageVolume`` resource can completely delete your storage volume just as easily as it can create it. To avoid costly accidents, consider setting [``preventDestroy``](/docs/configuration/resources.html#prevent_destroy) on your storage volume resources as an extra safety measure.

## Properties

`StorageType` - (Optional) - The Type of Storage to provision. Defaults to `/oracle/public/storage/default`.

`Bootable` - (Optional) Is the Volume Bootable? Defaults to `false`.

`ImageList` - (Optional) Defines an image list.

`ImageListEntry` - (Optional) Defines an image list entry.

`Snapshot` - (Optional) The name of the parent snapshot from which the storage volume is restored or cloned. See [Snapshots](#snapshots), below for more information.

`SnapshotId` - (Optional) The Id of the parent snapshot from which the storage volume is restored or cloned. See [Snapshots](#snapshots), below for more information.

`SnapshotAccount` - (Optional) The Account of the parent snapshot from which the storage volume is restored. See [Snapshots](#snapshots), below for more information.

`Tags` - (Optional) Comma-separated strings that tag the storage volume.


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