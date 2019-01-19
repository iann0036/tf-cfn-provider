# Terraform::UltraDNS::Dirpool

Provides an UltraDNS Directional Controller pool resource.

## Properties

`Zone` - (Required) The domain to add the record to.

`Name` - (Required) The name of the record - `Type` - (Required) The Record Type of the record.

`Type` - (Required) The Record Type of the record.

`Description` - (Required) Description of the Traffic Controller pool. Valid values are strings less than 256 characters.

`Rdata` - (Required) a list of Record Data blocks, one for each member in the pool. Record Data documented below.

`Ttl` - (Optional) The TTL of the record. Default: `3600`.

`ConflictResolve` - (Optional) String. Valid: `"GEO"` or `"IP"`. Default: `"GEO"`.

`NoResponse` - (Optional) a single Record Data block, without any `Host` attribute. Record Data documented below.

`Host` - (Required in `Rdata`, absent in `NoResponse`) IPv4 address or CNAME for the pool member. - `AllNonConfigured` - (Optional) Boolean. Default: `false`. - `GeoInfo` - (Optional) a single Geo Info block. Geo Info documented below. - `IpInfo` - (Optional) a single IP Info block. IP Info documented below.

`AllNonConfigured` - (Optional) Boolean. Default: `false`. - `GeoInfo` - (Optional) a single Geo Info block. Geo Info documented below. - `IpInfo` - (Optional) a single IP Info block. IP Info documented below.

`GeoInfo` - (Optional) a single Geo Info block. Geo Info documented below. - `IpInfo` - (Optional) a single IP Info block. IP Info documented below.

`IpInfo` - (Optional) a single IP Info block. IP Info documented below.

`Name` - (Optional) String. - `IsAccountLevel` - (Optional) Boolean. Default: `false`. - `Codes` - (Optional) Set of geo code strings. Shorthand codes are expanded.

`IsAccountLevel` - (Optional) Boolean. Default: `false`. - `Codes` - (Optional) Set of geo code strings. Shorthand codes are expanded.

`Codes` - (Optional) Set of geo code strings. Shorthand codes are expanded.

`Name` - (Optional) String. - `IsAccountLevel` - (Optional) Boolean. Default: `false`. - `Ips` - (Optional) Set of IP blocks. IP Info documented below.

`IsAccountLevel` - (Optional) Boolean. Default: `false`. - `Ips` - (Optional) Set of IP blocks. IP Info documented below.

`Ips` - (Optional) Set of IP blocks. IP Info documented below.

`Start` - (Optional) String. IP Address. Must be paired with `End`. Conflicts with `Cidr` or `Address`. - `End` - (Optional) String. IP Address. Must be paired with `Start`. - `Cidr` - (Optional) String. - `Address` - (Optional) String. IP Address.

`End` - (Optional) String. IP Address. Must be paired with `Start`. - `Cidr` - (Optional) String. - `Address` - (Optional) String. IP Address.

`Cidr` - (Optional) String. - `Address` - (Optional) String. IP Address.

`Address` - (Optional) String. IP Address.


## Return Values

### Fn::GetAtt

`Id` - The record ID.

`Hostname` - The FQDN of the record.

## See Also

* [ultradns_dirpool](https://www.terraform.io/docs/providers/ultradns/r/dirpool.html) in the _Terraform Provider Documentation_