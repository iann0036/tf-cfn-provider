# Terraform::Alicloud::PvtzZoneRecord

Provides a Private Zone Record resource.

-> **NOTE:** Terraform will auto Create a Private Zone Record while it uses `Terraform::Alicloud::PvtzZoneRecord` to build a Private Zone Record resource.

## Properties

`ZoneId` - (Required, Forces new resource) The name of the Private Zone Record.

`ResourceRecord` - (Required) The resource record of the Private Zone Record.

`Type` - (Required) The type of the Private Zone Record. Valid values: A, CNAME, TXT, MX, PTR.

`Value` - (Required) The value of the Private Zone Record.

`Ttl` - (Optional) The ttl of the Private Zone Record.

`Priority` - (Optional) The priority of the Private Zone Record. At present, only can "MX" record support it. Valid values: [1-50]. Default to 1.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Private Zone Record.

## See Also

* [alicloud_pvtz_zone_record](https://www.terraform.io/docs/providers/alicloud/r/pvtz_zone_record.html) in the _Terraform Provider Documentation_