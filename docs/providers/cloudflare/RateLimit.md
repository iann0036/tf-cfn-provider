# Terraform::Cloudflare::RateLimit

Provides a Cloudflare rate limit resource for a given zone. This can be used to limit the traffic you receive zone-wide, or matching more specific types of requests/responses.

## Properties

`Zone` - (Required) The DNS zone to apply rate limiting to.

`Threshold` - (Required) The threshold that triggers the rate limit mitigations, combine with period. i.e. threshold per period (min: 2, max: 1,000,000).

`Period` - (Required) The time in seconds to count matching traffic. If the count exceeds threshold within this period the action will be performed (min: 1, max: 86,400).

`Action` - (Required) The action to be performed when the threshold of matched traffic within the period defined is exceeded.

`Match` - (Optional) Determines which traffic the rate limit counts towards the threshold. By default matches all traffic in the zone. See definition below.

`Disabled` - (Optional) Whether this ratelimit is currently disabled. Default: `false`.

`Description` - (Optional) A note that you can use to describe the reason for a rate limit. This value is sanitized and all tags are removed.

`BypassUrlPatterns` - (Optional) URLs matching the patterns specified here will be excluded from rate limiting.

`Correlate` - (Optional) Determines how rate limiting is applied. By default if not specified, rate limiting applies to the clients IP address.

`Request` - (Optional) Matches HTTP requests (from the client to Cloudflare). See definition below.

`Methods` - (Optional) HTTP Methods, can be a subset ['POST','PUT'] or all ['\_ALL\_']. Default: ['\_ALL\_'].

`Schemes` - (Optional) HTTP Schemes, can be one ['HTTPS'], both ['HTTP','HTTPS'] or all ['\_ALL\_'].  Default: ['\_ALL\_'].

`UrlPattern` - (Optional) The URL pattern to match comprised of the host and path, i.e. example.org/path. Wildcard are expanded to match applicable traffic, query strings are not matched. Use * for all traffic to your zone. Default: '*'.

`Statuses` - (Optional) HTTP Status codes, can be one [403], many [401,403] or indicate all by not providing this value.

`OriginTraffic` - (Optional) Only count traffic that has come from your origin servers. If true, cached items that Cloudflare serve will not count towards rate limiting. Default: `true`.

`Mode` - (Required) The type of action to perform. Allowable values are 'simulate' and 'ban'.

`Timeout` - (Optional) The time in seconds as an integer to perform the mitigation action. This field is required if the `Mode` is either `simulate` or `ban`. Must be the same or greater than the period (min: 1, max: 86400).

`Response` - (Optional) Custom content-type and body to return, this overrides the custom error for the zone. This field is not required. Omission will result in default HTML error page. Definition below.

`ContentType` - (Required) The content-type of the body, must be one of: 'text/plain', 'text/xml', 'application/json'.

`Body` - (Required) The body to return, the content here should conform to the content_type.

`By` - (Optional) If set to 'nat', NAT support will be enabled for rate limiting.


## Return Values

### Fn::GetAtt

`Id` - The Rate limit ID.

`ZoneId` - The DNS zone ID.

## See Also

* [cloudflare_rate_limit](https://www.terraform.io/docs/providers/cloudflare/r/rate_limit.html) in the _Terraform Provider Documentation_