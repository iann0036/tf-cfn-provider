# Terraform::OpenTelekomCloud::DnsRecordsetV2

Manages a DNS record set in the OpenTelekomCloud DNS Service.

## Properties

`Region` - (Optional) The region in which to obtain the V2 DNS client.
If omitted, the `Region` argument of the provider is used.
Changing this creates a new DNS  record set.

`ZoneId` - (Required) The ID of the zone in which to create the record set.
Changing this creates a new DNS  record set.

`Name` - (Required) The name of the record set. Note the `.` at the end of the name.
Changing this creates a new DNS  record set.

`Type` - (Optional) The type of record set. Examples: "A", "MX".
Changing this creates a new DNS  record set.

`Ttl` - (Optional) The time to live (TTL) of the record set.

`Description` - (Optional) A description of the  record set.

`Records` - (Optional) An array of DNS records.

`ValueSpecs` - (Optional) Map of additional options. Changing this creates a
new record set.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`Type` - See Properties above.

`Ttl` - See Properties above.

`Description` - See Properties above.

`Records` - See Properties above.

`ZoneId` - See Properties above.

`ValueSpecs` - See Properties above.

## See Also

* [opentelekomcloud_dns_recordset_v2](https://www.terraform.io/docs/providers/opentelekomcloud/r/dns_recordset_v2.html) in the _Terraform Provider Documentation_