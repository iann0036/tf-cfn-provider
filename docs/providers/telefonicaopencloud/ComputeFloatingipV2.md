# Terraform::TelefonicaOpenCloud::ComputeFloatingipV2

Manages a V2 floating IP resource within TelefonicaOpenCloud Nova (compute)
that can be used for compute instances.

Please note that managing floating IPs through the TelefonicaOpenCloud Compute API has
been deprecated. Unless you are using an older TelefonicaOpenCloud environment, it is
recommended to use the [`telefonicaopencloud_networking_floatingip_v2`](networking_floatingip_v2.html)
resource instead, which uses the TelefonicaOpenCloud Networking API.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Region` - See Argument Reference above.

`Pool` - See Argument Reference above.

`Address` - The actual floating IP address itself.

`FixedIp` - The fixed IP address corresponding to the floating IP.

`InstanceId` - UUID of the compute instance associated with the floating IP.

## See Also

* [telefonicaopencloud_compute_floatingip_v2](https://www.terraform.io/docs/providers/telefonicaopencloud/r/compute_floatingip_v2.html) in the _Terraform Provider Documentation_