# Terraform::OpenTelekomCloud::NetworkingVipV2

Manages a V2 vip resource within OpenTelekomCloud.

## Properties

`NetworkId` - (Required) The ID of the network to attach the vip to. Changing this creates a new vip.

`SubnetId` - (Required) Subnet in which to allocate IP address for this vip. Changing this creates a new vip.

`IpAddress` - (Optional) IP address desired in the subnet for this vip. If you don't specify `IpAddress`, an available IP address from the specified subnet will be allocated to this vip.

`Name` - (Optional) A unique name for the vip.


## Return Values

### Fn::GetAtt

`NetworkId` - See Properties above.

`SubnetId` - See Properties above.

`IpAddress` - See Properties above.

`Name` - See Properties above.

`Status` - The status of vip.

`Id` - The ID of the vip.

`TenantId` - The tenant ID of the vip.

`DeviceOwner` - The device owner of the vip.

## See Also

* [opentelekomcloud_networking_vip_v2](https://www.terraform.io/docs/providers/opentelekomcloud/r/networking_vip_v2.html) in the _Terraform Provider Documentation_