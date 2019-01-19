# Terraform::Cloudflare::CustomPages

Provides a resource which manages Cloudflare custom error pages.

## Properties

`ZoneId` - (Optional) The zone ID where the custom pages should be updated. Either `ZoneId` or `AccountId` must be provided.

`AccountId` - (Optional) The account ID where the custom pages should be updated. Either `AccountId` or `ZoneId` must be provided. If `AccountId` is present, it will override the zone setting.

`Type` - (Required) The type of custom page you wish to update. Must be one of `basic_challenge`, `waf_challenge`, `waf_block`, `ratelimit_block`, `country_challenge`, `ip_block`, `under_attack`, `500_errors`, `1000_errors`, `always_online`.

`Url` - (Required) URL of where the custom page source is located.

`State` - (Required) Managed state of the custom page. Must be one of `default`, `customised`. If the value is `default` it will be removed from the Terraform state management.


## See Also

* [cloudflare_custom_pages](https://www.terraform.io/docs/providers/cloudflare/r/custom_pages.html) in the _Terraform Provider Documentation_