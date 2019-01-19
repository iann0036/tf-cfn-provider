# Terraform::DNS::MxRecordSet

Creates an MX type DNS record set.

## Properties

`Zone` - (Required) DNS zone the record set belongs to. It must be an FQDN, that is, include the trailing dot.

`Name` - (Optional) The name of the record set. The `Zone` argument will be appended to this value to create the full record path.

`Mx` - (Required) Can be specified multiple times for each MX record. Each block supports fields documented below.

`Ttl` - (Optional) The TTL of the record set. Defaults to `3600`.

`Preference` - (Required) The preference for the record.

`Exchange` - (Required) The FQDN of the mail exchange, include the trailing dot.


## Return Values

### Fn::GetAtt

`Zone` - See Properties above.

`Name` - See Properties above.

`Mx` - See Properties above.

`Ttl` - See Properties above.

## See Also

* [dns_mx_record_set](https://www.terraform.io/docs/providers/dns/r/mx_record_set.html) in the _Terraform Provider Documentation_