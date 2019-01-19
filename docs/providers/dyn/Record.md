# Terraform::Dyn::Record

Provides a Dyn DNS record resource.

## Properties

`Name` - (Required) The name of the record.

`Type` - (Required) The type of the record.

`Value` - (Required) The value of the record.

`Zone` - (Required) The DNS zone to add the record to.

`Ttl` - (Optional) The TTL of the record. Default uses the zone default.


## Return Values

### Fn::GetAtt

`Id` - The record ID.

`Fqdn` - The FQDN of the record, built from the `Name` and the `Zone`.

## See Also

* [dyn_record](https://www.terraform.io/docs/providers/dyn/r/record.html) in the _Terraform Provider Documentation_