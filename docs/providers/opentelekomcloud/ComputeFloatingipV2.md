# Terraform::OpenTelekomCloud::ComputeFloatingipV2

Manages a V2 floating IP resource within OpenTelekomCloud Nova (compute)
that can be used for compute instances.
These are similar to Neutron (networking) floating IP resources,
but only networking floating IPs can be used with load balancers.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Region` - See Argument Reference above.

`Pool` - See Argument Reference above.

`Address` - The actual floating IP address itself.

`FixedIp` - The fixed IP address corresponding to the floating IP.

`InstanceId` - UUID of the compute instance associated with the floating IP.

## See Also

* [opentelekomcloud_compute_floatingip_v2](https://www.terraform.io/docs/providers/opentelekomcloud/r/compute_floatingip_v2.html) in the _Terraform Provider Documentation_