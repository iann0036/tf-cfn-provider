# Terraform::Cobbler::Distro

Manages a distribution within Cobbler.

## Properties

`Arch` - (Required) The architecture of the distro. Valid options
are: i386, x86_64, ia64, ppc, ppc64, s390, arm.

`Breed` - (Required) The "breed" of distribution. Valid options
are: redhat, fedora, centos, scientific linux, suse, debian, and
ubuntu. These choices may vary depending on the version of Cobbler
in use.

`BootFiles` - (Optional) Files copied into tftpboot beyond the
kernel/initrd.

`Comment` - (Optional) Free form text description.

`FetchableFiles` - (Optional) Templates for tftp or wget.

`Kernel` - (Required) Absolute path to kernel on filesystem. This
must already exist prior to creating the distro.

`KernelOptions` - (Optional) Kernel options to use with the
kernel.

`KernelOptionsPost` - (Optional) Post install Kernel options to
use with the kernel after installation.

`Initrd` - (Required) Absolute path to initrd on filesystem. This
must already exist prior to creating the distro.

`MgmtClasses` - (Optional) Management classes for external config
management.

`Name` - (Required) A name for the distro.

`OsVersion` - (Required) The version of the distro you are
creating. This varies with the version of Cobbler you are using.
An updated signature list may need to be obtained in order to
support a newer version. Example: `trusty`.

`Owners` - (Optional) Owners list for authz_ownership.

`RedhatManagementKey` - (Optional) Red Hat Management key.

`RedhatManagementServer` - (Optional) Red Hat Management server.

`TemplateFiles` - (Optional) File mappings for built-in config
management.


## See Also

* [cobbler_distro](https://www.terraform.io/docs/providers/cobbler/r/distro.html) in the _Terraform Provider Documentation_