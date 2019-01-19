# Terraform::BIGIP::SysProvision

`BigipSysProvision` provides details bout how to enable "ilx", "asm" "apm" resource on BIG-IP

## Properties

`BigipSysProvision` - Is the resource which is used to provision big-ip modules like asm, afm, ilx etc.

`Common/ilx` - Common is the partition and ilx is the module being enabled it could be asm, afm apm etc.

`CpuRatio` - how much cpu resources you need for this resource.

`DiskRatio` - how much disk space you want to allocate for this resource.

`MemoryRatio` - how much memory you want to deidcate for this resource.


## See Also

* [bigip_sys_provision](https://www.terraform.io/docs/providers/bigip/r/sys_provision.html) in the _Terraform Provider Documentation_