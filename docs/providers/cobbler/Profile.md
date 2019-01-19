# Terraform::Cobbler::Profile

Manages a Profile within Cobbler.

## Properties

`BootFiles` - (Optional) Files copied into tftpboot beyond the kernel/initrd.

`Comment` - (Optional) Free form text description.

`Parent` - (Optional) The parent this profile inherits settings from.

`Server` - (Optional) The server-override for the profile.

`Distro` - (Optional) Parent distribution.

`EnableGpxe` - (Optional) Use gPXE instead of PXELINUX for advanced booting options.

`EnableMenu` - (Optional) Enable a boot menu.

`FetchableFiles` - (Optional) Templates for tftp or wget.

`KernelOptions` - (Optional) Kernel options for the profile.

`KernelOptionsPost` - (Optional) Post install kernel options.

`Kickstart` - (Optional) The kickstart file to use.

`KsMeta` - (Optional) Kickstart metadata.

`MgmtClasses` - (Optional) For external configuration management.

`MgmtParameters` - (Optional) Parameters which will be handed to your management application (Must be a valid YAML dictionary).

`NameServersSearch` - (Optional) Name server search settings.

`NameServers` - (Optional) Name servers.

`Name` - (Required) The name of the profile.

`Owners` - (Optional) Owners list for authz_ownership.

`Proxy` - (Optional) Proxy URL.

`RedhatManagementKey` - (Optional) Red Hat Management Key.

`RedhatManagementServer` - (Optional) RedHat Management Server.

`Repos` - (Optional) Repos to auto-assign to this profile.

`TemplateFiles` - (Optional) File mappings for built-in config management.

`TemplateRemoteKickstarts` - (Optional) remote kickstart templates.

`VirtAutoBoot` - (Optional) Auto boot virtual machines.

`VirtBridge` - (Optional) The bridge for virtual machines.

`VirtCpus` - (Optional) The number of virtual CPUs.

`VirtFileSize` - (Optional) The virtual machine file size.

`VirtPath` - (Optional) The virtual machine path.

`VirtRam` - (Optional) The amount of RAM for the virtual machine.

`VirtType` - (Optional) The type of virtual machine. Valid options are: xenpv, xenfv, qemu, kvm, vmware, openvz.

`VirtDiskDriver` - (Optional) The virtual machine disk driver.


## See Also

* [cobbler_profile](https://www.terraform.io/docs/providers/cobbler/r/profile.html) in the _Terraform Provider Documentation_