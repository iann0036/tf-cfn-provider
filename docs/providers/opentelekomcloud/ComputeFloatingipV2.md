# Terraform::OpenTelekomCloud::ComputeFloatingipV2

Manages a V2 floating IP resource within OpenTelekomCloud Nova (compute)
that can be used for compute instances.
These are similar to Neutron (networking) floating IP resources,
but only networking floating IPs can be used with load balancers.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Compute client. A Compute client is needed to create a floating IP that can be used with a compute instance. If omitted, the `Region` argument of the provider is used. Changing this creates a new floating IP (which may or may not have a different address).

`Pool` - (Required) The name of the pool from which to obtain the floating IP. Changing this creates a new floating IP.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Pool` - See Properties above.

`Address` - The actual floating IP address itself.

`FixedIp` - The fixed IP address corresponding to the floating IP.

`InstanceId` - UUID of the compute instance associated with the floating IP.

## See Also

* [opentelekomcloud_compute_floatingip_v2](https://www.terraform.io/docs/providers/opentelekomcloud/r/compute_floatingip_v2.html) in the _Terraform Provider Documentation_