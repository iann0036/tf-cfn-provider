# Terraform::Packet::IpAttachment

Provides a resource to attach elastic IP subnets to devices.

To attach an IP subnet from a reserved block to a provisioned device, you must derive a subnet CIDR belonging to
one of your reserved blocks in the same project and facility as the target device.

For example, you have reserved IPv4 address block 147.229.10.152/30, you can choose to assign either the whole
block as one subnet to a device; or 2 subnets with CIDRs 147.229.10.152/31' and 147.229.10.154/31; or 4 subnets
with mask prefix length 32. More about the elastic IP subnets is [here](https://help.packet.net/article/54-elastic-ips).

Device and reserved block must be in the same facility.

## Properties

`DeviceId` - (Required) ID of device to which to assign the subnet.

`CidrNotation` - (Required) CIDR notation of subnet from block reserved in the same project and facility as the device.


## Return Values

### Fn::GetAtt

`Id` - The unique ID of the assignment.

`DeviceId` - ID of device to which subnet is assigned.

`CidrNotation` - Assigned subnet in CIDR notation, e.g. "147.229.15.30/31".

`Gateway` - IP address of gateway for the subnet.

`Network` - Subnet network address.

`Netmask` - Subnet mask in decimal notation, e.g. "255.255.255.0".

`Cidr` - length of CIDR prefix of the subnet as integer.

`AddressFamily` - Address family as integer (4 or 6).

`Public` - boolean flag whether subnet is reachable from the Internet.

## See Also

* [packet_ip_attachment](https://www.terraform.io/docs/providers/packet/r/ip_attachment.html) in the _Terraform Provider Documentation_