# Terraform::OpenTelekomCloud::BlockstorageVolumeAttachV2

This resource is experimental and may be removed in the future! Feedback
is requested if you find this resource useful or if you find any problems
with it.

Creates a general purpose attachment connection to a Block
Storage volume using the OpenTelekomCloud Block Storage (Cinder) v2 API.
Depending on your Block Storage service configuration, this
resource can assist in attaching a volume to a non-OpenTelekomCloud resource
such as a bare-metal server or a remote virtual machine in a
different cloud provider.

This does not actually attach a volume to an instance. Please use
the `opentelekomcloud_compute_volume_attach_v2` resource for that.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Data` - This is a map of key/value pairs that contain the connection.

`DriverVolumeType` - The storage driver that the volume is based on.

`MountPointBase` - A mount point base name for shared storage.

## See Also

* [opentelekomcloud_blockstorage_volume_attach_v2](https://www.terraform.io/docs/providers/opentelekomcloud/r/blockstorage_volume_attach_v2.html) in the _Terraform Provider Documentation_