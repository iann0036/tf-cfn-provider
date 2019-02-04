# Terraform::Cobbler::Repo

Manages a repo within Cobbler.

## Properties

`AptComponents` - (Optional) List of Apt components such as main,
restricted, universe. Applicable to apt breeds only.

`AptDists` - (Optional) List of Apt distribution names such as trusty,
trusty-updates. Applicable to apt breeds only.

`Arch` - (Optional) The architecture of the repo. Valid options
are: i386, x86_64, ia64, ppc, ppc64, s390, arm.

`Breed` - (Required) The "breed" of distribution. Valid options
are: rsync, rhn, yum, apt, and wget. These choices may vary depending on the
version of Cobbler in use.

`Comment` - (Optional) Free form text description.

`CreaterepoFlags` - (Optional) Flags to use with `createrepo`.

`Environment` - (Optional) Environment variables to use during repo command
execution.

`KeepUpdated` - (Optional) Update the repo upon Cobbler sync. Valid values
are true or false.

`Mirror` - (Required) Address of the repo to mirror.

`MirrorLocally` - (Required) Whether to copy the files locally or just
references to the external files. Valid values are true or false.

`Name` - (Required) A name for the repo.

`Owners` - (Optional) List of Owners for authz_ownership.

`Proxy` - (Optional) Proxy to use for downloading the repo. This argument does
not work on older versions of Cobbler.

`RpmList` - (Optional) List of specific RPMs to mirror.


## See Also

* [cobbler_repo](https://www.terraform.io/docs/providers/cobbler/r/repo.html) in the _Terraform Provider Documentation_