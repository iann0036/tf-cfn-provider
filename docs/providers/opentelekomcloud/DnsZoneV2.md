# Terraform::OpenTelekomCloud::DnsZoneV2

Manages a DNS zone in the OpenTelekomCloud DNS Service.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Compute client. Keypairs are associated with accounts, but a Compute client is needed to create one. If omitted, the `Region` argument of the provider is used. Changing this creates a new DNS zone.

`Name` - (Required) The name of the zone. Note the `.` at the end of the name. Changing this creates a new DNS zone.

`Email` - (Optional) The email contact for the zone record.

`Type` - (Optional) The type of zone. Can either be `public` or `private`. Changing this creates a new zone.

`Ttl` - (Optional) The time to live (TTL) of the zone.

`Description` - (Optional) A description of the zone.

`Masters` - (Optional) An array of master DNS servers.

`ValueSpecs` - (Optional) Map of additional options. Changing this creates a new zone.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`Email` - See Properties above.

`Type` - See Properties above.

`Ttl` - See Properties above.

`Description` - See Properties above.

`Masters` - See Properties above.

`ValueSpecs` - See Properties above.

## See Also

* [opentelekomcloud_dns_zone_v2](https://www.terraform.io/docs/providers/opentelekomcloud/r/dns_zone_v2.html) in the _Terraform Provider Documentation_