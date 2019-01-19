# Terraform::DNS::CnameRecord

Creates a CNAME type DNS record.

## Properties

`Zone` - (Required) DNS zone the record belongs to. It must be an FQDN, that is, include the trailing dot.

`Name` - (Required) The name of the record. The `Zone` argument will be appended to this value to create the full record path.

`Cname` - (Required) The canonical name this record will point to.

`Ttl` - (Optional) The TTL of the record set. Defaults to `3600`.


## Return Values

### Fn::GetAtt

`Zone` - See Properties above.

`Name` - See Properties above.

`Cname` - See Properties above.

`Ttl` - See Properties above.

## See Also

* [dns_cname_record](https://www.terraform.io/docs/providers/dns/r/cname_record.html) in the _Terraform Provider Documentation_