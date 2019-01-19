# Terraform::DNS::NsRecordSet

Creates a NS type DNS record set.

## Properties

`Zone` - (Required) DNS zone the record set belongs to. It must be an FQDN, that is, include the trailing dot.

`Name` - (Required) The name of the record set. The `Zone` argument will be appended to this value to create the full record path.

`Nameservers` - (Required) The nameservers this record set will point to.

`Ttl` - (Optional) The TTL of the record set. Defaults to `3600`.


## Return Values

### Fn::GetAtt

`Zone` - See Properties above.

`Name` - See Properties above.

`Nameservers` - See Properties above.

`Ttl` - See Properties above.

## See Also

* [dns_ns_record_set](https://www.terraform.io/docs/providers/dns/r/ns_record_set.html) in the _Terraform Provider Documentation_