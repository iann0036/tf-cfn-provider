# Terraform::Packet::ReservedIpBlock

Provides a resource to create and manage blocks of reserved IP addresses in a project.

When user provision first device in a facility, Packet automatically allocates IPv6/56 and private IPv4/25 blocks.
The new device then gets IPv6 and private IPv4 addresses from those block. It also gets a public IPv4/31 address.
Every new device in the project and facility will automatically get IPv6 and private IPv4 addresses from pre-allocated i
blocks.
The IPv6 and private IPv4 blocks can't be created, only imported.

It is only possible to create public IPv4 blocks, with masks from /24 (256 addresses) to /32 (1 address).

Once IP block is allocated or imported, an address from it can be assigned to device with the `packet_ip_attachment` resource.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Facility` - The facility where the addresses are.

`ProjectId` - To which project the addresses beling.

`Quantity` - Number of /32 addresses in the block.

`Id` - The unique ID of the block.

`CidrNotation` - Address and mask in CIDR notation, e.g. "147.229.15.30/31".

`Network` - Network IP address portion of the block specification.

`Netmask` - Mask in decimal notation, e.g. "255.255.255.0".

`Cidr` - length of CIDR prefix of the block as integer.

`AddressFamily` - Address family as integer (4 or 6).

`Public` - boolean flag whether addresses from a block are public.

## See Also

* [packet_reserved_ip_block](https://www.terraform.io/docs/providers/packet/r/reserved_ip_block.html) in the _Terraform Provider Documentation_