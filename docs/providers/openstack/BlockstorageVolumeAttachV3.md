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
the `Terraform::OpenStack::ComputeVolumeAttachV3` resource for that.

## Properties

`Region` - (Optional) The region in which to obtain the V3 Block Storage client. A Block Storage client is needed to create a volume attachment. If omitted, the `Region` argument of the provider is used. Changing this creates a new volume attachment.

`AttachMode` - (Optional) Specify whether to attach the volume as Read-Only (`ro`) or Read-Write (`rw`). Only values of `ro` and `rw` are accepted. If left unspecified, the Block Storage API will apply a default of `rw`.

`Device` - (Optional) The device to tell the Block Storage service this volume will be attached as. This is purely for informational purposes. You can specify `auto` or a device such as `/dev/vdc`.

`HostName` - (Required) The host to attach the volume to.

`Initiator` - (Optional) The iSCSI initiator string to make the connection.

`IpAddress` - (Optional) The IP address of the `HostName` above.

`Multipath` - (Optional) Whether to connect to this volume via multipath.

`OsType` - (Optional) The iSCSI initiator OS type.

`Platform` - (Optional) The iSCSI initiator platform.

`VolumeId` - (Required) The ID of the Volume to attach to an Instance.

`Wwpn` - (Optional) An array of wwpn strings. Used for Fibre Channel connections.

`Wwnn` - (Optional) A wwnn name. Used for Fibre Channel connections.


## Return Values

### Fn::GetAtt

`Data` - This is a map of key/value pairs that contain the connection.

`DriverVolumeType` - The storage driver that the volume is based on.

`MountPointBase` - A mount point base name for shared storage.

## See Also

* [openstack_blockstorage_volume_attach_v3](https://www.terraform.io/docs/providers/openstack/r/blockstorage_volume_attach_v3.html) in the _Terraform Provider Documentation_