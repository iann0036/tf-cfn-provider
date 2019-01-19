# Terraform::NS1::Record

Provides a NS1 Record resource. This can be used to create, modify, and delete records.

## Properties

`Zone` - (Required) The zone the record belongs to.

`Domain` - (Required) The records' domain.

`Type` - (Required) The records' RR type.

`Ttl` - (Optional) The records' time to live.

`Link` - (Optional) The target record to link to. This means this record is a 'linked' record, and it inherits all properties from its target.

`UseClientSubnet` - (Optional) Whether to use EDNS client subnet data when available(in filter chain).

`Answers` - (Optional) One or more NS1 answers for the records' specified type. Answers are documented below.

`Filters` - (Optional) One or more NS1 filters for the record(order matters). Filters are documented below.

`Answer` - (Required) Space delimited string of RDATA fields dependent on the record type.

`Region` - (Optional) The region(or group) name that this answer belongs to.

`Filter` - (Required) The type of filter.

`Disabled` - (Optional) Determines whether the filter is applied in the filter chain.

`Config` - (Optional) The filters' configuration. Simple key/value pairs determined by the filter type.


## See Also

* [ns1_record](https://www.terraform.io/docs/providers/ns1/r/record.html) in the _Terraform Provider Documentation_