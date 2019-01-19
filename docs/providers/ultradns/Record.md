# Terraform::UltraDNS::Record

Provides an UltraDNS record resource.

## Properties

`Zone` - (Required) The domain to add the record to.

`Name` - (Required) The name of the record.

`Rdata` - (Required) An array containing the values of the record.

`Type` - (Required) The type of the record.

`Ttl` - (Optional) The TTL of the record.


## Return Values

### Fn::GetAtt

`Id` - The record ID.

`Name` - The name of the record.

`Rdata` - An array containing the values of the record.

`Type` - The type of the record.

`Ttl` - The TTL of the record.

`Zone` - The domain of the record.

`Hostname` - The FQDN of the record.

## See Also

* [ultradns_record](https://www.terraform.io/docs/providers/ultradns/r/record.html) in the _Terraform Provider Documentation_