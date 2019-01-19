# Terraform::OVH::DomainZoneRecord

Provides a OVH domain zone record.

## Properties

`Zone` - (Required) The domain to add the record to.

`Subdomain` - (Required) The name of the record.

`Target` - (Required) The value of the record.

`Fieldtype` - (Required) The type of the record.

`Ttl` - (Optional) The TTL of the record.


## Return Values

### Fn::GetAtt

`Id` - The record ID.

`Zone` - The domain to add the record to.

`SubDomain` - The name of the record.

`Target` - The value of the record.

`FieldType` - The type of the record.

`Ttl` - The TTL of the record.

## See Also

* [ovh_domain_zone_record](https://www.terraform.io/docs/providers/ovh/r/domain_zone_record.html) in the _Terraform Provider Documentation_