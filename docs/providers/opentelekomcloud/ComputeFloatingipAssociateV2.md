# Terraform::OpenTelekomCloud::ComputeFloatingipAssociateV2

Associate a floating IP to an instance. This can be used instead of the
`FloatingIp` options in `Terraform::OpenTelekomCloud::ComputeInstanceV2`.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Compute client.
Keypairs are associated with accounts, but a Compute client is needed to
create one. If omitted, the `Region` argument of the provider is used.
Changing this creates a new floatingip_associate.

`FloatingIp` - (Required) The floating IP to associate.

`InstanceId` - (Required) The instance to associte the floating IP with.

`FixedIp` - (Optional) The specific IP address to direct traffic to.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`FloatingIp` - See Properties above.

`InstanceId` - See Properties above.

`FixedIp` - See Properties above.

## See Also

* [opentelekomcloud_compute_floatingip_associate_v2](https://www.terraform.io/docs/providers/opentelekomcloud/r/compute_floatingip_associate_v2.html) in the _Terraform Provider Documentation_