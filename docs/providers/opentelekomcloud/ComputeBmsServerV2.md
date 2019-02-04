# Terraform::OpenTelekomCloud::ComputeBmsServerV2

Manages a BMS Server resource within OpenTelekomCloud.

## Properties

`Region` - (Optional) The region in which to create the bms server instance. If
omitted, the `Region` argument of the provider is used. Changing this
creates a new bms server.

`Name` - (Required) The name of the BMS.

`ImageId` - (Optional; Required if `ImageName` is empty.) Changing this creates a new bms server.

`ImageName` - (Optional; Required if `ImageId` is empty.) The name of the
desired image for the bms server. Changing this creates a new bms server.

`FlavorId` - (Optional; Required if `FlavorName` is empty) The flavor ID of
the desired flavor for the bms server. Changing this resizes the existing bms server.

`FlavorName` - (Optional; Required if `FlavorId` is empty) The name of the
desired flavor for the bms server. Changing this resizes the existing bms server.

`UserData` - (Optional) The user data to provide when launching the instance.
Changing this creates a new bms server.

`SecurityGroups` - (Optional) An array of one or more security group names
to associate with the bms server. Changing this results in adding/removing
security groups from the existing bms server.

`AvailabilityZone` - (Required) The availability zone in which to create
the bms server.

`Network` - (Optional) An array of one or more networks to attach to the
bms instance. Changing this creates a new bms server.

`Metadata` - (Optional) Metadata key/value pairs to make available from
within the instance. Changing this updates the existing bms server metadata.

`AdminPass` - (Optional) The administrative password to assign to the bms server.
Changing this changes the root password on the existing server.

`KeyPair` - (Optional) The name of a key pair to put on the bms server. The key
pair must already be created and associated with the tenant's account.
Changing this creates a new bms server.

`StopBeforeDestroy` - (Optional) Whether to try stop instance gracefully
before destroying it, thus giving chance for guest OS daemons to stop correctly.
If instance doesn't stop within timeout, it will be destroyed anyway.

### Network Properties

`Uuid` - (Required unless `Port`  or `Name` is provided) The network UUID to
attach to the bms server. Changing this creates a new bms server.

`Name` - (Required unless `Uuid` or `Port` is provided) The human-readable
name of the network. Changing this creates a new bms server.

`Port` - (Required unless `Uuid` or `Name` is provided) The port UUID of a
network to attach to the bms server. Changing this creates a new server.

`FixedIpV4` - (Optional) Specifies a fixed IPv4 address to be used on this
network. Changing this creates a new bms server.

`FixedIpV6` - (Optional) Specifies a fixed IPv6 address to be used on this
network. Changing this creates a new bms server.

`AccessNetwork` - (Optional) Specifies if this network should be used for
provisioning access. Accepts true or false. Defaults to false.

`Id` - The id of the bms server.

`ConfigDrive` - Whether to use the config_drive feature to configure the instance.

`KernelId` - The UUID of the kernel image when the AMI image is used.

`UserId` - The ID of the user to which the BMS belongs.

`HostStatus` - The nova-compute status: **UP, UNKNOWN, DOWN, MAINTENANCE** and **Null**.


## See Also

* [opentelekomcloud_compute_bms_server_v2](https://www.terraform.io/docs/providers/opentelekomcloud/r/compute_bms_server_v2.html) in the _Terraform Provider Documentation_