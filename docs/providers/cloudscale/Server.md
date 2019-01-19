# Terraform::CloudScale::Server

Provides a cloudscale.ch Server resource. This can be used to create, modify, and delete servers.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The UUID of this server.

`Href` - The cloudscale.ch API URL of the current resource.

`SshFingerprints` - A list of SSH host key fingerprints (strings) of this server.

`SshHostKeys` - A list of SSH host keys (strings) of this server.

`AntiAffinityWith` - A list of server UUIDs that belong to the same anti-affinity group as this server.

`Volumes` - A list of volume objects attached to this server. Each volume object has three attributes:.

`DevicePath` - The path (string) to the volume on your server (e.g. `/dev/vda`).

`SizeGb` - The size (int) of the volume in GB. Typically matches `volume_size_gb` or `bulk_volume_size_gb`.

`Type` - Either `public` or `private`. Public interfaces are connected to the Internet, while private interfaces are not.

`Interfaces` - A list of interface objects attached to this server. Each interface object has two attributes:.

`Addresses` - A list of address objects:.

`Address` - An IPv4 or IPv6 address that has been assigned to this server.

`Gateway` - An IPv4 or IPv6 address that represents the default gateway for this interface.

`PrefixLength` - The prefix length for this IP address, typically 24 for IPv4 and 128 for IPv6.

`ReversePtr` - The PTR record (reverse DNS pointer) for this IP address. If you use an FQDN as your server name it will automatically be used here.

`Version` - The IP version, either `4` or `6`.

## See Also

* [cloudscale_server](https://www.terraform.io/docs/providers/cloudscale/r/server.html) in the _Terraform Provider Documentation_