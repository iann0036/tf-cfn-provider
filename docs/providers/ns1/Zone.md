# Terraform::NS1::Zone

Provides a NS1 DNS Zone resource. This can be used to create, modify, and delete zones.

## Properties

`Zone` - (Required) The domain name of the zone.

`Link` - (Optional) The target zone(domain name) to link to.

`Ttl` - (Optional) The SOA TTL.

`Refresh` - (Optional) The SOA Refresh.

`Retry` - (Optional) The SOA Retry.

`Expiry` - (Optional) The SOA Expiry.

`NxTtl` - (Optional) The SOA NX TTL.

`Primary` - (Optional) The primary zones' ip. This makes the zone a secondary.


## See Also

* [ns1_zone](https://www.terraform.io/docs/providers/ns1/r/zone.html) in the _Terraform Provider Documentation_