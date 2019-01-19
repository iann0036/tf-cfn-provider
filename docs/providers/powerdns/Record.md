# Terraform::PowerDNS::Record

Provides a PowerDNS record resource.

## Properties

`Zone` - (Required) The name of zone to contain this record.

`Name` - (Required) The name of the record.

`Type` - (Required) The record type.

`Ttl` - (Required) The TTL of the record.

`Records` - (Required) A string list of records.


## See Also

* [powerdns_record](https://www.terraform.io/docs/providers/powerdns/r/record.html) in the _Terraform Provider Documentation_