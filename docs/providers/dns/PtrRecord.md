# Terraform::DNS::PtrRecord

Creates a PTR type DNS record.

## Properties

`Zone` - (Required) DNS zone the record belongs to. It must be an FQDN, that is, include the trailing dot.

`Name` - (Optional) The name of the record. The `Zone` argument will be appended to this value to create the full record path.

`Ptr` - (Required) The canonical name this record will point to.

`Ttl` - (Optional) The TTL of the record set. Defaults to `3600`.


## Return Values

### Fn::GetAtt

`Zone` - See Properties above.

`Name` - See Properties above.

`Ptr` - See Properties above.

`Ttl` - See Properties above.

## See Also

* [dns_ptr_record](https://www.terraform.io/docs/providers/dns/r/ptr_record.html) in the _Terraform Provider Documentation_