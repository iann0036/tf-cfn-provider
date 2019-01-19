# Terraform::DNS::ARecordSet

Creates a A type DNS record set.

## Properties

`Zone` - (Required) DNS zone the record set belongs to. It must be an FQDN, that is, include the trailing dot.

`Name` - (Optional) The name of the record set. The `Zone` argument will be appended to this value to create the full record path.

`Addresses` - (Required) The IPv4 addresses this record set will point to.

`Ttl` - (Optional) The TTL of the record set. Defaults to `3600`.


## Return Values

### Fn::GetAtt

`Zone` - See Properties above.

`Name` - See Properties above.

`Addresses` - See Properties above.

`Ttl` - See Properties above.

## See Also

* [dns_a_record_set](https://www.terraform.io/docs/providers/dns/r/a_record_set.html) in the _Terraform Provider Documentation_