# Terraform::FlexibleEngine::NetworkingPortV2

Manages a V2 port resource within FlexibleEngine.

## Properties

`Region` - (Optional) The region in which to obtain the V2 networking client.
A networking client is needed to create a port. If omitted, the
`Region` argument of the provider is used. Changing this creates a new
port.

`Name` - (Optional) A unique name for the port. Changing this
updates the `Name` of an existing port.

`NetworkId` - (Required) The ID of the network to attach the port to. Changing
this creates a new port.

`AdminStateUp` - (Optional) Administrative up/down status for the port
(must be "true" or "false" if provided). Changing this updates the
`AdminStateUp` of an existing port.

`MacAddress` - (Optional) Specify a specific MAC address for the port. Changing
this creates a new port.

`TenantId` - (Optional) The owner of the Port. Required if admin wants
to create a port for another tenant. Changing this creates a new port.

`DeviceOwner` - (Optional) The device owner of the Port. Changing this creates
a new port.

`SecurityGroupIds` - (Optional) A list of security group IDs to apply to the
port. The security groups must be specified by ID and not name (as opposed
to how they are configured with the Compute Instance).

`DeviceId` - (Optional) The ID of the device attached to the port. Changing this
creates a new port.

`FixedIp` - (Optional) An array of desired IPs for this port. The structure is
described below.

`AllowedAddressPairs` - (Optional) An IP/MAC Address pair of additional IP
addresses that can be active on this port. The structure is described
below.

`ValueSpecs` - (Optional) Map of additional options.

### FixedIp Properties

`SubnetId` - (Required) Subnet in which to allocate IP address for
this port.

`IpAddress` - (Optional) IP address desired in the subnet for this port. If
you don't specify `IpAddress`, an available IP address from the specified
subnet will be allocated to this port.

### AllowedAddressPairs Properties

`IpAddress` - (Required) The additional IP address.

`MacAddress` - (Optional) The additional MAC address.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`AdminStateUp` - See Properties above.

`MacAddress` - See Properties above.

`TenantId` - See Properties above.

`DeviceOwner` - See Properties above.

`SecurityGroupIds` - See Properties above.

`DeviceId` - See Properties above.

`FixedIp` - See Properties above.

`All fixedIps` - The collection of Fixed IP addresses on the port in the.

## See Also

* [flexibleengine_networking_port_v2](https://www.terraform.io/docs/providers/flexibleengine/r/networking_port_v2.html) in the _Terraform Provider Documentation_