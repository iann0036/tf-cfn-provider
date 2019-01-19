# Terraform::Cloudflare::RateLimit

Provides a Cloudflare rate limit resource for a given zone. This can be used to limit the traffic you receive zone-wide, or matching more specific types of requests/responses.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - The Rate limit ID.

`ZoneId` - The DNS zone ID.

## See Also

* [cloudflare_rate_limit](https://www.terraform.io/docs/providers/cloudflare/r/rate_limit.html) in the _Terraform Provider Documentation_