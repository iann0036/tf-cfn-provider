# Terraform::Alicloud::DiskAttachment

Provides an Alicloud ECS Disk Attachment as a resource, to attach and detach disks from ECS Instances.

## Properties

`InstanceId` - (Required, Forces new resource) ID of the Instance to attach to.

`DiskId` - (Required, Forces new resource) ID of the Disk to be attached.

`DeviceName` - (Deprecated) The device name has been deprecated, and when attaching disk, it will be allocated automatically by system according to default order from /dev/xvdb to /dev/xvdz.


## Return Values

### Fn::GetAtt

`InstanceId` - ID of the Instance.

`DiskId` - ID of the Disk.

`DeviceName` - The device name exposed to the instance.

## See Also

* [alicloud_disk_attachment](https://www.terraform.io/docs/providers/alicloud/r/disk_attachment.html) in the _Terraform Provider Documentation_