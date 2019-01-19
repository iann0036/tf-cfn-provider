# Terraform::Cloudflare::Record

Provides a Cloudflare record resource.

## Properties

`Domain` - (Required) The DNS zone to add the record to.

`Name` - (Required) The name of the record.

`Type` - (Required) The type of the record.

`Value` - (Optional) The (string) value of the record. Either this or `Data` must be specified.

`Data` - (Optional) Map of attributes that constitute the record value. Primarily used for LOC and SRV record types. Either this or `Value` must be specified.

`Ttl` - (Optional) The TTL of the record ([automatic: '1'](https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record)).

`Priority` - (Optional) The priority of the record.

`Proxied` - (Optional) Whether the record gets Cloudflare's origin protection; defaults to `false`.


## Return Values

### Fn::GetAtt

`Id` - The record ID.

`Hostname` - The FQDN of the record.

`Proxiable` - Shows whether this record can be proxied, must be true if setting `proxied=true`.

`CreatedOn` - The RFC3339 timestamp of when the record was created.

`ModifiedOn` - The RFC3339 timestamp of when the record was last modified.

`Metadata` - A key-value map of string metadata cloudflare associates with the record.

`ZoneId` - The zone id of the record.

## See Also

* [cloudflare_record](https://www.terraform.io/docs/providers/cloudflare/r/record.html) in the _Terraform Provider Documentation_