# Terraform::Cloudflare::ZoneLockdown

Provides a Cloudflare Zone Lockdown resource. Zone Lockdown allows you to define one or more URLs (with wildcard matching on the domain or path) that will only permit access if the request originates from an IP address that matches a safelist of one or more IP addresses and/or IP ranges.

## Properties

`Zone` - The DNS zone to which the lockdown will be added. Will be resolved to `ZoneId` upon creation.

`ZoneId` - The DNS zone to which the access rule should be added.

`Description` - (Optional) A description about the lockdown entry. Typically used as a reminder or explanation for the lockdown.

`Urls` - (Required) A list of simple wildcard patterns to match requests against. The order of the urls is unimportant.

`Configurations` - (Required) A list of IP addresses or IP ranges to match the request against specified in target, value pairs.  It's a complex value. See description below.   The order of the configuration entries is unimportant.

`Paused` - (Optional) Boolean of whether this zone lockdown is currently paused. Default: false.

`Target` - (Required) The request property to target. Allowed values: "ip", "ip_range".

`Value` - (Required) The value to target. Depends on target's type. IP addresses should just be standard IPv4/IPv6 notation i.e. `198.51.100.4` or `2001:db8::/32` and IP ranges in CIDR format i.e. `198.51.0.0/16`.


## Return Values

### Fn::GetAtt

`Id` - The access rule ID.

## See Also

* [cloudflare_zone_lockdown](https://www.terraform.io/docs/providers/cloudflare/r/zone_lockdown.html) in the _Terraform Provider Documentation_