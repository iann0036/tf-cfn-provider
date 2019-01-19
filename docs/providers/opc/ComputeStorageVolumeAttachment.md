# Terraform::OPC::ComputeStorageVolumeAttachment

The `Terraform::OPC::ComputeStorageVolumeAttachment` resource creates and manages a storage volume attachment in an Oracle Cloud Infrastructure Compute Classic identity domain.

## Properties

`Instance` - (Required) The name of the instance the volume will be attached to.

`StorageVolume` - (Required) The name of the storage volume that will be attached to the instance.

`Index` - (Required) The index on the instance that the storage volume will be attached to.


## See Also

* [opc_compute_storage_volume_attachment](https://www.terraform.io/docs/providers/opc/r/compute_storage_volume_attachment.html) in the _Terraform Provider Documentation_