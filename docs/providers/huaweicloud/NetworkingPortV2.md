# Terraform::HuaweiCloud::NetworkingPortV2

Manages a V2 port resource within HuaweiCloud.

## Properties

`Region` - (Optional) The region in which to obtain the V2 networking client. A networking client is needed to create a port. If omitted, the `Region` argument of the provider is used. Changing this creates a new port.

`Name` - (Optional) A unique name for the port. Changing this updates the `Name` of an existing port.

`NetworkId` - (Required) The ID of the network to attach the port to. Changing this creates a new port.

`AdminStateUp` - (Optional) Administrative up/down status for the port (must be "true" or "false" if provided). Changing this updates the `AdminStateUp` of an existing port.

`MacAddress` - (Optional) The additional MAC address.

`TenantId` - (Optional) The owner of the Port. Required if admin wants to create a port for another tenant. Changing this creates a new port.

`DeviceOwner` - (Optional) The device owner of the Port. Changing this creates a new port.

`SecurityGroupIds` - (Optional - Conflicts with `NoSecurityGroups`) A list of security group IDs to apply to the port. The security groups must be specified by ID and not name (as opposed to how they are configured with the Compute Instance).

`NoSecurityGroups` - (Optional - Conflicts with `SecurityGroupIds`) If set to `true`, then no security groups are applied to the port. If set to `false` and no `SecurityGroupIds` are specified, then the Port will yield to the default behavior of the Networking service, which is to usually apply the "default" security group.

`DeviceId` - (Optional) The ID of the device attached to the port. Changing this creates a new port.

`FixedIp` - (Optional) An array of desired IPs for this port. The structure is described below.

`AllowedAddressPairs` - (Optional) An IP/MAC Address pair of additional IP addresses that can be active on this port. The structure is described below.

`ValueSpecs` - (Optional) Map of additional options.

`SubnetId` - (Required) Subnet in which to allocate IP address for this port.

`IpAddress` - (Required) The additional IP address.


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

`AllFixedIps` - The collection of Fixed IP addresses on the port in the.

`AllSecurityGroupIds` - The collection of Security Group IDs on the port.

## See Also

* [huaweicloud_networking_port_v2](https://www.terraform.io/docs/providers/huaweicloud/r/networking_port_v2.html) in the _Terraform Provider Documentation_