# Terraform::DigitalOcean::Record

Provides a DigitalOcean DNS record resource.

## Properties

`Type` - (Required) The type of record. Must be one of `A`, `AAAA`, `CAA`, `CNAME`, `MX`, `NS`, `TXT`, or `SRV`.

`Domain` - (Required) The domain to add the record to.

`Value` - (Required) The value of the record.

`Name` - (Required) The name of the record.

`Port` - (Optional) The port of the record. Only valid when type is `SRV`.  Must be between 1 and 65535.

`Priority` - (Optional) The priority of the record. Only valid when type is `MX` or `SRV`. Must be between 0 and 65535.

`Weight` - (Optional) The weight of the record. Only valid when type is `SRV`.  Must be between 0 and 65535.

`Ttl` - (Optional) The time to live for the record, in seconds. Must be at least 0.

`Flags` - (Optional) The flags of the record. Only valid when type is `CAA`. Must be between 0 and 255.

`Tag` - (Optional) The tag of the record. Only valid when type is `CAA`. Must be one of `issue`, `wildissue`, or `iodef`.


## Return Values

### Fn::GetAtt

`Id` - The record ID.

`Fqdn` - The FQDN of the record.

## See Also

* [digitalocean_record](https://www.terraform.io/docs/providers/digitalocean/r/record.html) in the _Terraform Provider Documentation_