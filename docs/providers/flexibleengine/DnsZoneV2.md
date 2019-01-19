# Terraform::FlexibleEngine::DnsZoneV2

Manages a DNS zone in the FlexibleEngine DNS Service.

## Properties

`Region` - (Optional) The region in which to obtain the V2 Compute client. Keypairs are associated with accounts, but a Compute client is needed to create one. If omitted, the `Region` argument of the provider is used. Changing this creates a new DNS zone. Changing this creates a new DNS zone.

`Name` - (Required) The name of the zone. Note the `.` at the end of the name. Changing this creates a new DNS zone.

`Email` - (Optional) The email contact for the zone record. Changing this creates a new DNS zone.

`ZoneType` - (Optional) The type of zone. Can either be `public` or `private`. Changing this creates a new DNS zone.

`Router` - (Optional) Router configuration block which is required if zone_type is private. The router structure is documented below.  Changing this creates a new DNS zone.

`Ttl` - (Optional) The time to live (TTL) of the zone. Changing this creates a new DNS zone.

`Description` - (Optional) A description of the zone. Changing this creates a new DNS zone.

`ValueSpecs` - (Optional) Map of additional options. Changing this creates a new DNS zone.

`RouterId` - (Required) The router UUID. Changing this creates a new DNS zone.

`RouterRegion` - (Required) The region of the router. Changing this creates a new DNS zone.


## Return Values

### Fn::GetAtt

`Region` - See Properties above.

`Name` - See Properties above.

`Email` - See Properties above.

`ZoneType` - See Properties above.

`Ttl` - See Properties above.

`Description` - See Properties above.

`Masters` - An array of master DNS servers.

`ValueSpecs` - See Properties above.

## See Also

* [flexibleengine_dns_zone_v2](https://www.terraform.io/docs/providers/flexibleengine/r/dns_zone_v2.html) in the _Terraform Provider Documentation_