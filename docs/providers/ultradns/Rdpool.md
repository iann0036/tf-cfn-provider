# Terraform::UltraDNS::Rdpool

Provides an UltraDNS Resource Distribution (RD) pool resource, which are
used to define rules for returning multiple A or AAAA records for a given owner name. Ordering can be FIXED, RANDOM or ROUND_ROBIN.

## Properties

`Zone` - (Required) The domain to add the record to.

`Name` - (Required) The name of the record.

`Rdata` - (Required) list ip addresses.

`Order` - (Optional) Ordering rule, one of FIXED, RANDOM or ROUND_ROBIN. Default: 'ROUND_ROBIN'.

`Description` - (Optional) Description of the Resource Distribution pool. Valid values are strings less than 256 characters.

`Ttl` - (Optional) The TTL of the pool in seconds. Default: `3600`.


## Return Values

### Fn::GetAtt

`Id` - The record ID.

`Hostname` - The FQDN of the record.

## See Also

* [ultradns_rdpool](https://www.terraform.io/docs/providers/ultradns/r/rdpool.html) in the _Terraform Provider Documentation_