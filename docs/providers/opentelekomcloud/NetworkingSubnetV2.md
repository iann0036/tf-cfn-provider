# Terraform::OpenTelekomCloud::NetworkingSubnetV2

Manages a V2 Neutron subnet resource within OpenTelekomCloud.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnet. If omitted, the
`Region` argument of the provider is used. Changing this creates a new
subnet.

`NetworkId` - (Required) The UUID of the parent network. Changing this
creates a new subnet.

`Cidr` - (Required) CIDR representing IP range for this subnet, based on IP
version. Changing this creates a new subnet.

`IpVersion` - (Optional) IP version, either 4 (default) or 6. Changing this creates a
new subnet.

`Name` - (Optional) The name of the subnet. Changing this updates the name of
the existing subnet.

`TenantId` - (Optional) The owner of the subnet. Required if admin wants to
create a subnet for another tenant. Changing this creates a new subnet.

`AllocationPools` - (Optional) An array of sub-ranges of CIDR available for
dynamic allocation to ports. The allocation_pool object structure is
documented below. Changing this creates a new subnet.

`GatewayIp` - (Optional)  Default gateway used by devices in this subnet.
Leaving this blank and not setting `NoGateway` will cause a default
gateway of `.1` to be used. Changing this updates the gateway IP of the
existing subnet.

`NoGateway` - (Optional) Do not set a gateway IP on this subnet. Changing
this removes or adds a default gateway IP of the existing subnet.

`EnableDhcp` - (Optional) The administrative state of the network.
Acceptable values are "true" and "false". Changing this value enables or
disables the DHCP capabilities of the existing subnet. Defaults to true.

`DnsNameservers` - (Optional) An array of DNS name server names used by hosts
in this subnet. Changing this updates the DNS name servers for the existing
subnet.

`HostRoutes` - (Optional) An array of routes that should be used by devices
with IPs from this subnet (not including local subnet route). The host_route
object structure is documented below. Changing this updates the host routes
for the existing subnet.

`ValueSpecs` - (Optional) Map of additional options.

### AllocationPools Properties

`Start` - (Required) The starting address.

`End` - (Required) The ending address.

### HostRoutes Properties

`DestinationCidr` - (Required) The destination CIDR.

`NextHop` - (Required) The next hop in the route.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`NetworkId` - See Properties above.

`Cidr` - See Properties above.

`IpVersion` - See Properties above.

`Name` - See Properties above.

`TenantId` - See Properties above.

`AllocationPools` - See Properties above.

`GatewayIp` - See Properties above.

`EnableDhcp` - See Properties above.

`DnsNameservers` - See Properties above.

`HostRoutes` - See Properties above.

## See Also

* [opentelekomcloud_networking_subnet_v2](https://www.terraform.io/docs/providers/opentelekomcloud/r/networking_subnet_v2.html) in the _Terraform Provider Documentation_