# Terraform::Alicloud::PvtzZone

Provides a Private Zone resource.

~> **NOTE:** Terraform will auto Create a Private Zone while it uses `Terraform::Alicloud::PvtzZone` to build a Private Zone resource.

## Properties

`Name` - (Required, Forces new resource) The name of the Private Zone.

`Remark` - (Optional) The remark of the Private Zone.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Private Zone.

`RecordCount` - The count of the Private Zone Record.

## See Also

* [alicloud_pvtz_zone](https://www.terraform.io/docs/providers/alicloud/r/pvtz_zone.html) in the _Terraform Provider Documentation_