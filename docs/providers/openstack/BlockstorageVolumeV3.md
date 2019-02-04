# Terraform::OpenStack::BlockstorageVolumeV3

Manages a V3 volume resource within OpenStack.

## Properties

`Region` - (Optional) The region in which to create the volume. If
omitted, the `Region` argument of the provider is used. Changing this
creates a new volume.

`Size` - (Required) The size of the volume to create (in gigabytes).

`EnableOnlineResize` - (Optional) When this option is set it allows extending
attached volumes. Note: updating size of an attached volume requires Cinder
support for version 3.42 and a compatible storage driver.

`AvailabilityZone` - (Optional) The availability zone for the volume.
Changing this creates a new volume.

`ConsistencyGroupId` - (Optional) The consistency group to place the volume
in.

`Description` - (Optional) A description of the volume. Changing this updates
the volume's description.

`ImageId` - (Optional) The image ID from which to create the volume.
Changing this creates a new volume.

`Metadata` - (Optional) Metadata key/value pairs to associate with the volume.
Changing this updates the existing volume metadata.

`Name` - (Optional) A unique name for the volume. Changing this updates the
volume's name.

`SnapshotId` - (Optional) The snapshot ID from which to create the volume.
Changing this creates a new volume.

`SourceReplica` - (Optional) The volume ID to replicate with.

`SourceVolId` - (Optional) The volume ID from which to create the volume.
Changing this creates a new volume.

`VolumeType` - (Optional) The type of volume to create.
Changing this creates a new volume.

`Multiattach` - (Optional) Allow the volume to be attached to more than one Compute instance.


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

`Multiattach` - See Properties above.

## See Also

* [openstack_blockstorage_volume_v3](https://www.terraform.io/docs/providers/openstack/r/blockstorage_volume_v3.html) in the _Terraform Provider Documentation_