# Terraform::CloudScale::Server

Provides a cloudscale.ch Server resource. This can be used to create, modify, and delete servers.

## Properties

`Name` - (Required) Name of the new server. The name has to be a valid host name or a fully qualified domain name (FQDN).

`FlavorSlug` - (Required) The slug (name) of the flavor to use for the new server. Possible values can be found in our [API documentation](https://www.cloudscale.ch/en/api/v1#flavors).

`ImageSlug` - (Required) The slug (name) of the image to use for the new server. Possible values can be found in our [API documentation](https://www.cloudscale.ch/en/api/v1#images).

`SshKeys` - (Required) A list of SSH public keys. Use the full content of your \*.pub file here.

`VolumeSizeGb` - (Optional) The size in GB of the SSD root volume of the new server. If this parameter is not specified, the value will be set to 10. Valid values are either 10 or multiples of 50.

`BulkVolumeSizeGb` - (Optional) The size in GB of the bulk storage volume of the new server. If this parameter is not specified, no bulk storage volume will be attached to the server. Valid values are multiples of 100.

`UsePublicNetwork` - (Optional) Attach/detach the public network interface to/from the new server. Can be `true` (default) or `false`.

`UsePrivateNetwork` - (Optional) Attach/detach the private network interface to/from the new server. Can be `true` or `false` (default).

`UseIpv6` - (Optional) Enable/disable IPv6 on the public network interface of the new server. Can be `true` (default) or `false`.

`AntiAffinityUuid` - (Optional) Pass the UUID of another server to either create a new anti-affinity group with that server or add the new server to the same (existing) group as the other server.

`UserData` - (Optional) User data (custom cloud-config settings) to use for the new server. Needs to be valid YAML. A default configuration will be used if this parameter is not specified or set to null. Use only if you are an advanced user with knowledge of cloud-config and cloud-init.

`Status` - (Optional) The desired state of a server. Can be `running` (default) or `stopped`.

`Status` - (Optional) The desired state of a server. Can be `running` (default) or `stopped`.


## Return Values

### Fn::GetAtt

`Id` - The UUID of this server.

`Href` - The cloudscale.ch API URL of the current resource.

`SshFingerprints` - A list of SSH host key fingerprints (strings) of this server.

`SshHostKeys` - A list of SSH host keys (strings) of this server.

`AntiAffinityWith` - A list of server UUIDs that belong to the same anti-affinity group as this server.

`Volumes` - A list of volume objects attached to this server. Each volume object has three attributes:.

`DevicePath` - The path (string) to the volume on your server (e.g. `/dev/vda`).

`SizeGb` - The size (int) of the volume in GB. Typically matches `VolumeSizeGb` or `BulkVolumeSizeGb`.

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