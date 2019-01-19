# Terraform::DNS::TxtRecordSet

Creates a TXT type DNS record set.

## Properties

`Zone` - (Required) DNS zone the record set belongs to. It must be an FQDN, that is, include the trailing dot.

`Name` - (Optional) The name of the record set. The `Zone` argument will be appended to this value to create the full record path.

`Txt` - (Required) The text records this record set will be set to.

`Ttl` - (Optional) The TTL of the record set. Defaults to `3600`.


## Return Values

### Fn::GetAtt

`Zone` - See Properties above.

`Name` - See Properties above.

`Txt` - See Properties above.

`Ttl` - See Properties above.

## See Also

* [dns_txt_record_set](https://www.terraform.io/docs/providers/dns/r/txt_record_set.html) in the _Terraform Provider Documentation_