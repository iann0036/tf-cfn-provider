# Terraform::CloudStack::Disk

Creates a disk volume from a disk offering. This disk volume will be attached to
a virtual machine if the optional parameters are configured.

## Properties

`Name` - (Required) The name of the disk volume. Changing this forces a new resource to be created.

`Attach` - (Optional) Determines whether or not to attach the disk volume to a virtual machine (defaults false).

`DeviceId` - (Optional) The device ID to map the disk volume to within the guest OS.

`DiskOffering` - (Required) The name or ID of the disk offering to use for this disk volume.

`Size` - (Optional) The size of the disk volume in gigabytes.

`ShrinkOk` - (Optional) Verifies if the disk volume is allowed to shrink when resizing (defaults false).

`VirtualMachineId` - (Optional) The ID of the virtual machine to which you want to attach the disk volume.

`Project` - (Optional) The name or ID of the project to deploy this instance to. Changing this forces a new resource to be created.

`Zone` - (Required) The name or ID of the zone where this disk volume will be available. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The ID of the disk volume.

`DeviceId` - The device ID the disk volume is mapped to within the guest OS.

## See Also

* [cloudstack_disk](https://www.terraform.io/docs/providers/cloudstack/r/disk.html) in the _Terraform Provider Documentation_