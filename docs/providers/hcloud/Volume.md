# Terraform::HCloud::Volume

Provides a Hetzner Cloud volume resource to manage volumes.

## Properties

`Name` - (Required, string) Name of the volume to create (must be unique per project).
- `Size` - (Required, int) Size of the volume (in GB).
- `Server` - (Optional, int) Server to attach the Volume to, optional if location argument is passed.
- `Location` - (Optional, string) Location of the volume to create, optional if server_id argument is passed.
- `Automount` - (Optional, bool) Automount the volume upon attaching it (server_id must be provided).
- `Format` - (Optional, string) Format volume after creation. `xfs` or `ext4`.

`Size` - (Required, int) Size of the volume (in GB).
- `Server` - (Optional, int) Server to attach the Volume to, optional if location argument is passed.
- `Location` - (Optional, string) Location of the volume to create, optional if server_id argument is passed.
- `Automount` - (Optional, bool) Automount the volume upon attaching it (server_id must be provided).
- `Format` - (Optional, string) Format volume after creation. `xfs` or `ext4`.

`Server` - (Optional, int) Server to attach the Volume to, optional if location argument is passed.
- `Location` - (Optional, string) Location of the volume to create, optional if server_id argument is passed.
- `Automount` - (Optional, bool) Automount the volume upon attaching it (server_id must be provided).
- `Format` - (Optional, string) Format volume after creation. `xfs` or `ext4`.

`Location` - (Optional, string) Location of the volume to create, optional if server_id argument is passed.
- `Automount` - (Optional, bool) Automount the volume upon attaching it (server_id must be provided).
- `Format` - (Optional, string) Format volume after creation. `xfs` or `ext4`.

`Automount` - (Optional, bool) Automount the volume upon attaching it (server_id must be provided).
- `Format` - (Optional, string) Format volume after creation. `xfs` or `ext4`.

`Format` - (Optional, string) Format volume after creation. `xfs` or `ext4`.


## See Also

* [hcloud_volume](https://www.terraform.io/docs/providers/hcloud/r/volume.html) in the _Terraform Provider Documentation_