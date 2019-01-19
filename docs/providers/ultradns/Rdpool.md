# Terraform::UltraDNS::Rdpool

Provides an UltraDNS Resource Distribution (RD) pool resource, which are
used to define rules for returning multiple A or AAAA records for a given owner name. Ordering can be FIXED, RANDOM or ROUND_ROBIN.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The record ID.

`Hostname` - The FQDN of the record.

## See Also

* [ultradns_rdpool](https://www.terraform.io/docs/providers/ultradns/r/rdpool.html) in the _Terraform Provider Documentation_