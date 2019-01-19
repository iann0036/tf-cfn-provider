# Terraform::Alicloud::Havip

Provides a HaVip resource.

~> **NOTE:** Terraform will auto build havip instance  while it uses `Terraform::Alicloud::Havip` to build a havip resource.

## Properties

`VswitchId` - (Required, ForceNew) The vswitch_id of the HaVip, the field can't be changed.

`IpAddress` - (Optional, ForceNew) The ip address of the HaVip. If not filled, the default will be assigned one from the vswitch.

`Description` - (Optional) The description of the HaVip instance.


## Return Values

### Fn::GetAtt

`Id` - The ID of the HaVip instance id.

## See Also

* [alicloud_havip](https://www.terraform.io/docs/providers/alicloud/r/havip.html) in the _Terraform Provider Documentation_