# Terraform::OpenTelekomCloud::NetworkingFloatingipV2

Manages a V2 floating IP resource within OpenTelekomCloud Neutron (networking)
that can be used for load balancers.
These are similar to Nova (compute) floating IP resources,
but only compute floating IPs can be used with compute instances.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Region` - See Argument Reference above.

`Pool` - See Argument Reference above.

`Address` - The actual floating IP address itself.

`PortId` - ID of associated port.

`TenantId` - the ID of the tenant in which to create the floating IP.

`FixedIp` - The fixed IP which the floating IP maps to.

## See Also

* [opentelekomcloud_networking_floatingip_v2](https://www.terraform.io/docs/providers/opentelekomcloud/r/networking_floatingip_v2.html) in the _Terraform Provider Documentation_