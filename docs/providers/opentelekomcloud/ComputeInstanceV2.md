# Terraform::OpenTelekomCloud::ComputeInstanceV2

Manages a V2 VM instance resource within OpenTelekomCloud.

## Properties

`Region` - (Optional) The region in which to create the server instance. If
omitted, the `Region` argument of the provider is used. Changing this
creates a new server.

`Name` - (Required) A unique name for the resource.

`ImageId` - (Optional; Required if `ImageName` is empty and not booting
from a volume. Do not specify if booting from a volume.) The image ID of
the desired image for the server. Changing this creates a new server.

`ImageName` - (Optional; Required if `ImageId` is empty and not booting
from a volume. Do not specify if booting from a volume.) The name of the
desired image for the server. Changing this creates a new server.

`FlavorId` - (Optional; Required if `FlavorName` is empty) The flavor ID of
the desired flavor for the server. Changing this resizes the existing server.

`FlavorName` - (Optional; Required if `FlavorId` is empty) The name of the
desired flavor for the server. Changing this resizes the existing server.

`UserData` - (Optional) The user data to provide when launching the instance.
Changing this creates a new server.

`SecurityGroups` - (Optional) An array of one or more security group names
to associate with the server. Changing this creates a new server.

`AvailabilityZone` - (Optional) The availability zone in which to create
the server. Changing this creates a new server.

`Network` - (Optional) An array of one or more networks to attach to the
instance. Required when there are multiple networks defined for the tenant.
The network object structure is documented below. Changing this creates a
new server.

`Metadata` - (Optional) Metadata key/value pairs to make available from
within the instance. Changing this updates the existing server metadata.

`ConfigDrive` - (Optional) Whether to use the config_drive feature to
configure the instance. Changing this creates a new server.

`AdminPass` - (Optional) The administrative password to assign to the server.
Changing this changes the root password on the existing server.

`KeyPair` - (Optional) The name of a key pair to put on the server. The key
pair must already be created and associated with the tenant's account.
Changing this creates a new server.

`BlockDevice` - (Optional) Configuration of block devices. The block_device
structure is documented below. Changing this creates a new server.
You can specify multiple block devices which will create an instance with
multiple disks. This configuration is very flexible, so please see the
following [reference](http://docs.openstack.org/developer/nova/block_device_mapping.html)
for more information.

`SchedulerHints` - (Optional) Provide the Nova scheduler with hints on how
the instance should be launched. The available hints are described below.

`Personality` - (Optional) Customize the personality of an instance by
defining one or more files and their contents. The personality structure
is described below.

`Tags` - **DEPRECATED** (Optional) The tags of the image. It must be a list of strings.

`Tag` - (Optional) Tags key/value pairs to associate with the instance.

`StopBeforeDestroy` - (Optional) Whether to try stop instance gracefully
before destroying it, thus giving chance for guest OS daemons to stop correctly.
If instance doesn't stop within timeout, it will be destroyed anyway.

`ForceDelete` - (Optional) Whether to force the OpenTelekomCloud instance to be
forcefully deleted. This is useful for environments that have reclaim / soft
deletion enabled.

`AutoRecovery` - (Optional) Configures or deletes automatic recovery of an instance.

### Network Properties

`Uuid` - (Required unless `Port`  or `Name` is provided) The network UUID to
attach to the server. Changing this creates a new server.

`Name` - (Required unless `Uuid` or `Port` is provided) The human-readable
name of the network. Changing this creates a new server.

`Port` - (Required unless `Uuid` or `Name` is provided) The port UUID of a
network to attach to the server. Changing this creates a new server.

`FixedIpV4` - (Optional) Specifies a fixed IPv4 address to be used on this
network. Changing this creates a new server.

`FixedIpV6` - (Optional) Specifies a fixed IPv6 address to be used on this
network. Changing this creates a new server.

`AccessNetwork` - (Optional) Specifies if this network should be used for
provisioning access. Accepts true or false. Defaults to false.

### BlockDevice Properties

`Uuid` - (Required unless `SourceType` is set to `"blank"` ) The UUID of
the image, volume, or snapshot. Changing this creates a new server.

`SourceType` - (Required) The source type of the device. Must be one of
"blank", "image", "volume", or "snapshot". Changing this creates a new
server.

`VolumeSize` - The size of the volume to create (in gigabytes). Required
in the following combinations: source=image and destination=volume,
and source=blank and destination=volume. Changing this creates a new server.

`VolumeType` - (Optional) Currently, the value can be `SSD` (ultra-I/O disk type), `SAS` (high I/O disk type), or `SATA` (common I/O disk type)
[OTC-API](https://docs.otc.t-systems.com/en-us/api/ecs/en-us_topic_0065817708.html).

`BootIndex` - (Optional) The boot index of the volume. It defaults to 0.
Changing this creates a new server.

`DestinationType` - (Optional) The type that gets created. Currently only
support "volume". Changing this creates a new server.

`DeleteOnTermination` - (Optional) Delete the volume / block device upon
termination of the instance. Defaults to false. Changing this creates a
new server.

### SchedulerHints Properties

`Group` - (Optional) A UUID of a Server Group. The instance will be placed
into that group.

`DifferentHost` - (Optional) A list of instance UUIDs. The instance will
be scheduled on a different host than all other instances.

`SameHost` - (Optional) A list of instance UUIDs. The instance will be
scheduled on the same host of those specified.

`Query` - (Optional) A conditional query that a compute node must pass in
order to host an instance.

`TargetCell` - (Optional) The name of a cell to host the instance.

`BuildNearHostIp` - (Optional) An IP Address in CIDR form. The instance
will be placed on a compute node that is in the same subnet.

`Tenancy` - (Optional) The tenancy specifies whether the ECS is to be created on a Dedicated Host
(DeH) or in a shared pool.

`DehId` - (Optional) The ID of DeH. This parameter takes effect only when the value
of tenancy is dedicated.

### Personality Properties

`File` - (Required) The absolute path of the destination file.

`Contents` - (Required) The contents of the file. Limited to 255 bytes.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`AccessIpV4` - The first detected Fixed IPv4 address _or_ the.

`AccessIpV6` - The first detected Fixed IPv6 address.

`Metadata` - See Properties above.

`SecurityGroups` - See Properties above.

`FlavorId` - See Properties above.

`FlavorName` - See Properties above.

`Network/uuid` - See Properties above.

`Network/name` - See Properties above.

`Network/port` - See Properties above.

`Network/fixedIpV4` - The Fixed IPv4 address of the Instance on that.

`Network/fixedIpV6` - The Fixed IPv6 address of the Instance on that.

`Network/mac` - The MAC address of the NIC on that network.

`AllMetadata` - Contains all instance metadata, even metadata not set.

`AutoRecovery` - See Properties above.

## See Also

* [opentelekomcloud_compute_instance_v2](https://www.terraform.io/docs/providers/opentelekomcloud/r/compute_instance_v2.html) in the _Terraform Provider Documentation_