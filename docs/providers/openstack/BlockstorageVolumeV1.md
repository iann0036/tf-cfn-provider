# Terraform::OpenStack::BlockstorageVolumeV1

Manages a V1 volume resource within OpenStack.

## Properties

`Region` - (Optional) The region in which to create the volume. If omitted, the `Region` argument of the provider is used. Changing this creates a new volume.

`Size` - (Required) The size of the volume to create (in gigabytes). Changing this creates a new volume.

`Name` - (Optional) A unique name for the volume. Changing this updates the volume's name.

`Description` - (Optional) A description of the volume. Changing this updates the volume's description.

`AvailabilityZone` - (Optional) The availability zone for the volume. Changing this creates a new volume.

`ImageId` - (Optional) The image ID from which to create the volume. Changing this creates a new volume.

`SnapshotId` - (Optional) The snapshot ID from which to create the volume. Changing this creates a new volume.

`SourceVolId` - (Optional) The volume ID from which to create the volume. Changing this creates a new volume.

`Metadata` - (Optional) Metadata key/value pairs to associate with the volume. Changing this updates the existing volume metadata.

`VolumeType` - (Optional) The type of volume to create. Changing this creates a new volume.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Size` - See Properties above.

`Name` - See Properties above.

`Description` - See Properties above.

`AvailabilityZone` - See Properties above.

`ImageId` - See Properties above.

`SourceVolId` - See Properties above.

`SnapshotId` - See Properties above.

`Metadata` - See Properties above.

`VolumeType` - See Properties above.

`Attachment` - If a volume is attached to an instance, this attribute will.

## See Also

* [openstack_blockstorage_volume_v1](https://www.terraform.io/docs/providers/openstack/r/blockstorage_volume_v1.html) in the _Terraform Provider Documentation_