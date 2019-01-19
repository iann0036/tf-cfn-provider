# Terraform::CloudStack::Disk

Creates a disk volume from a disk offering. This disk volume will be attached to
a virtual machine if the optional parameters are configured.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The ID of the disk volume.

`DeviceId` - The device ID the disk volume is mapped to within the guest OS.

## See Also

* [cloudstack_disk](https://www.terraform.io/docs/providers/cloudstack/r/disk.html) in the _Terraform Provider Documentation_