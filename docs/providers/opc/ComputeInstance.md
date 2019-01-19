# Terraform::OPC::ComputeInstance

The ``Terraform::OPC::ComputeInstance`` resource creates and manages an instance in an Oracle Cloud Infrastructure Compute Classic identity domain.

~> **Caution:** The ``Terraform::OPC::ComputeInstance`` resource can completely delete your
instance just as easily as it can create it. To avoid costly accidents,
consider setting
[``prevent_destroy``](/docs/configuration/resources.html#prevent_destroy)
on your instance resources as an extra safety measure.

## Properties

`Name` - (Required) The name of the instance.

`Shape` - (Required) The shape of the instance, e.g. `oc4`.

`InstanceAttributes` - (Optional) A JSON string of custom attributes. See [Attributes](#attributes) below for more information.

`BootOrder` - (Optional) The index number of the bootable storage volume, presented as a list, that should be used to boot the instance. The only valid value is `[1]`. If you set this attribute, you must also specify a bootable storage volume with index number 1 in the volume sub-parameter of storage_attachments. When you specify boot_order, you don't need to specify the imagelist attribute, because the instance is booted using the image on the specified bootable storage volume. If you specify both boot_order and imagelist, the imagelist attribute is ignored.

`Hostname` - (Optional) The host name assigned to the instance. On an Oracle Linux instance, this host name is displayed in response to the hostname command. Only relative DNS is supported. The domain name is suffixed to the host name that you specify. The host name must not end with a period. If you don't specify a host name, then a name is generated automatically.

`ImageList` - (Optional) The imageList of the instance, e.g. `/oracle/public/oel_6.4_2GB_v1`.

`Label` - (Optional) The label to apply to the instance.

`DesiredState` - (Optional) Set the desire state of the instance to `running` (default) or `shutdown`. You can use this request to shut down and restart individual instances which use a persistent bootable storage volume.

`NetworkingInfo` - (Optional) Information pertaining to an individual network interface to be created and attached to the instance. If left unspecified, the instance will be created within the `shared_network`. See [Networking Info](#networking-info) below for more information.

`Storage` - (Optional) Information pertaining to an individual storage attachment to be created during instance creation. Please see [Storage Attachments](#storage-attachments) below for more information.

`ReverseDns` - (Optional) If set to `true` (default), then reverse DNS records are created. If set to `false`, no reverse DNS records are created.

`SshKeys` - (Optional) A list of the names of the SSH Keys that can be used to log into the instance.

`Tags` - (Optional) A list of strings that should be supplied to the instance as tags.


## Return Values

### Fn::GetAtt

`Id` - The `id` of the instance.

`Attributes` - The full attributes of the instance, as a JSON string.

`AvailabilityDomain` - The availability domain the instance is in.

`Domain` - The default domain to use for the hostname and for DNS lookups.

`Entry` - Imagelist entry number.

`Fingerprint` - SSH server fingerprint presented by the instance.

`Fqdn` - The fully qualified domain name of the instance.

`ImageFormat` - The format of the image.

`IpAddress` - The IP Address of the instance.

`PlacementRequirements` - The array of placement requirements for the instance.

`Platform` - The OS Platform of the instance.

`Priority` - The priority at which the instance was ran.

`QuotaReservation` - Reference to the QuotaReservation, to be destroyed with the instance.

`Relationships` - The array of relationship specifications to be satisfied on instance placement.

`Resolvers` - Array of resolvers to be used instead of the default resolvers.

`Site` - The site the instance is running on.

`StartTime` - The launch time of the instance.

`State` - The instance's state.

`VcableId` - vCable ID for the instance.

`Virtio` - Boolean that determines if the instance is a virtio device.

`VncAddress` - The VNC address and port of the instance.

## See Also

* [opc_compute_instance](https://www.terraform.io/docs/providers/opc/r/compute_instance.html) in the _Terraform Provider Documentation_