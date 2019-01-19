# Terraform::Cloudflare::Record

Provides a Cloudflare record resource.

## Properties

TBC

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