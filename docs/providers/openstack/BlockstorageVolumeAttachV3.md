# Terraform::OpenStack::BlockstorageVolumeAttachV3

This resource is experimental and may be removed in the future! Feedback
is requested if you find this resource useful or if you find any problems
with it.

Creates a general purpose attachment connection to a Block
Storage volume using the OpenStack Block Storage (Cinder) v3 API.
Depending on your Block Storage service configuration, this
resource can assist in attaching a volume to a non-OpenStack resource
such as a bare-metal server or a remote virtual machine in a
different cloud provider.

This does not actually attach a volume to an instance. Please use
the `openstack_compute_volume_attach_v3` resource for that.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Data` - This is a map of key/value pairs that contain the connection.

`DriverVolumeType` - The storage driver that the volume is based on.

`MountPointBase` - A mount point base name for shared storage.

## See Also

* [openstack_blockstorage_volume_attach_v3](https://www.terraform.io/docs/providers/openstack/r/blockstorage_volume_attach_v3.html) in the _Terraform Provider Documentation_