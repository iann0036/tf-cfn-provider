# Terraform::TelefonicaOpenCloud::ComputeFloatingipV2

Manages a V2 floating IP resource within TelefonicaOpenCloud Nova (compute)
that can be used for compute instances.

Please note that managing floating IPs through the TelefonicaOpenCloud Compute API has
been deprecated. Unless you are using an older TelefonicaOpenCloud environment, it is
recommended to use the [`Terraform::TelefonicaOpenCloud::NetworkingFloatingipV2`](networking_floatingip_v2.html)
resource instead, which uses the TelefonicaOpenCloud Networking API.

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

* [telefonicaopencloud_compute_floatingip_v2](https://www.terraform.io/docs/providers/telefonicaopencloud/r/compute_floatingip_v2.html) in the _Terraform Provider Documentation_