# Terraform::HCloud::Server

Provides an Hetzner Cloud server resource. This can be used to create, modify, and delete servers. Servers also support [provisioning](https://www.terraform.io/docs/provisioners/index.html).

## Properties

`Name` - (Required, string) Name of the server to create (must be unique per project and a valid hostname as per RFC 1123).
- `ServerType` - (Required, string) Name of the server type this server should be created with.
- `Image` - (Required, string) Name or ID of the image the server is created from.
- `Location` - (Optional, string) The location name to create the server in. `nbg1`, `fsn1` or `hel1`
- `Datacenter` - (Optional, string) The datacenter name to create the server in.
- `UserData` - (Optional, string) Cloud-Init user data to use during server creation
- `SshKeys` - (Optional, list) SSH key IDs or names which should be injected into the server at creation time
- `KeepDisk` - (Optional, bool) If true, do not upgrade the disk. This allows downgrading the server type later.
- `Iso` - (Optional, string) Name of an ISO image to mount.
- `Rescue` - (Optional, string) Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
- `Labels` - (Optional, map) User-defined labels (key-value pairs) should be created with.
- `Backups` - (Optional, boolean) Enable or disable backups.

`ServerType` - (Required, string) Name of the server type this server should be created with.
- `Image` - (Required, string) Name or ID of the image the server is created from.
- `Location` - (Optional, string) The location name to create the server in. `nbg1`, `fsn1` or `hel1`
- `Datacenter` - (Optional, string) The datacenter name to create the server in.
- `UserData` - (Optional, string) Cloud-Init user data to use during server creation
- `SshKeys` - (Optional, list) SSH key IDs or names which should be injected into the server at creation time
- `KeepDisk` - (Optional, bool) If true, do not upgrade the disk. This allows downgrading the server type later.
- `Iso` - (Optional, string) Name of an ISO image to mount.
- `Rescue` - (Optional, string) Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
- `Labels` - (Optional, map) User-defined labels (key-value pairs) should be created with.
- `Backups` - (Optional, boolean) Enable or disable backups.

`Image` - (Required, string) Name or ID of the image the server is created from.
- `Location` - (Optional, string) The location name to create the server in. `nbg1`, `fsn1` or `hel1`
- `Datacenter` - (Optional, string) The datacenter name to create the server in.
- `UserData` - (Optional, string) Cloud-Init user data to use during server creation
- `SshKeys` - (Optional, list) SSH key IDs or names which should be injected into the server at creation time
- `KeepDisk` - (Optional, bool) If true, do not upgrade the disk. This allows downgrading the server type later.
- `Iso` - (Optional, string) Name of an ISO image to mount.
- `Rescue` - (Optional, string) Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
- `Labels` - (Optional, map) User-defined labels (key-value pairs) should be created with.
- `Backups` - (Optional, boolean) Enable or disable backups.

`Location` - (Optional, string) The location name to create the server in. `nbg1`, `fsn1` or `hel1`
- `Datacenter` - (Optional, string) The datacenter name to create the server in.
- `UserData` - (Optional, string) Cloud-Init user data to use during server creation
- `SshKeys` - (Optional, list) SSH key IDs or names which should be injected into the server at creation time
- `KeepDisk` - (Optional, bool) If true, do not upgrade the disk. This allows downgrading the server type later.
- `Iso` - (Optional, string) Name of an ISO image to mount.
- `Rescue` - (Optional, string) Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
- `Labels` - (Optional, map) User-defined labels (key-value pairs) should be created with.
- `Backups` - (Optional, boolean) Enable or disable backups.

`Datacenter` - (Optional, string) The datacenter name to create the server in.
- `UserData` - (Optional, string) Cloud-Init user data to use during server creation
- `SshKeys` - (Optional, list) SSH key IDs or names which should be injected into the server at creation time
- `KeepDisk` - (Optional, bool) If true, do not upgrade the disk. This allows downgrading the server type later.
- `Iso` - (Optional, string) Name of an ISO image to mount.
- `Rescue` - (Optional, string) Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
- `Labels` - (Optional, map) User-defined labels (key-value pairs) should be created with.
- `Backups` - (Optional, boolean) Enable or disable backups.

`UserData` - (Optional, string) Cloud-Init user data to use during server creation
- `SshKeys` - (Optional, list) SSH key IDs or names which should be injected into the server at creation time
- `KeepDisk` - (Optional, bool) If true, do not upgrade the disk. This allows downgrading the server type later.
- `Iso` - (Optional, string) Name of an ISO image to mount.
- `Rescue` - (Optional, string) Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
- `Labels` - (Optional, map) User-defined labels (key-value pairs) should be created with.
- `Backups` - (Optional, boolean) Enable or disable backups.

`SshKeys` - (Optional, list) SSH key IDs or names which should be injected into the server at creation time
- `KeepDisk` - (Optional, bool) If true, do not upgrade the disk. This allows downgrading the server type later.
- `Iso` - (Optional, string) Name of an ISO image to mount.
- `Rescue` - (Optional, string) Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
- `Labels` - (Optional, map) User-defined labels (key-value pairs) should be created with.
- `Backups` - (Optional, boolean) Enable or disable backups.

`KeepDisk` - (Optional, bool) If true, do not upgrade the disk. This allows downgrading the server type later.
- `Iso` - (Optional, string) Name of an ISO image to mount.
- `Rescue` - (Optional, string) Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
- `Labels` - (Optional, map) User-defined labels (key-value pairs) should be created with.
- `Backups` - (Optional, boolean) Enable or disable backups.

`Iso` - (Optional, string) Name of an ISO image to mount.
- `Rescue` - (Optional, string) Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
- `Labels` - (Optional, map) User-defined labels (key-value pairs) should be created with.
- `Backups` - (Optional, boolean) Enable or disable backups.

`Rescue` - (Optional, string) Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
- `Labels` - (Optional, map) User-defined labels (key-value pairs) should be created with.
- `Backups` - (Optional, boolean) Enable or disable backups.

`Labels` - (Optional, map) User-defined labels (key-value pairs) should be created with.
- `Backups` - (Optional, boolean) Enable or disable backups.

`Backups` - (Optional, boolean) Enable or disable backups.


## See Also

* [hcloud_server](https://www.terraform.io/docs/providers/hcloud/r/server.html) in the _Terraform Provider Documentation_