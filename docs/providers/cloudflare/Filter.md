# Terraform::Cloudflare::Filter

Filter expressions that can be referenced across multiple features, e.g. [Firewall Rule](firewall_rule.html). The expression format is similar to [Wireshark Display Filter](https://www.wireshark.org/docs/man-pages/wireshark-filter.html).

## Properties

`Zone` - (Optional) The DNS zone to which the Filter should be added. Will be resolved to `ZoneId` upon creation.

`ZoneId` - (Optional) The DNS zone to which the Filter should be added.

`Paused` - (Optional) Whether this filter is currently paused. Boolean value.

`Expression` - (Required) The filter expression to be used.

`Description` - (Optional) A note that you can use to describe the purpose of the filter.

`Ref` - (Optional) Short reference tag to quickly select related rules.


## Return Values

### Fn::GetAtt

`Id` - Filter identifier.

`ZoneId` - The DNS zone ID.

## See Also

* [cloudflare_filter](https://www.terraform.io/docs/providers/cloudflare/r/filter.html) in the _Terraform Provider Documentation_