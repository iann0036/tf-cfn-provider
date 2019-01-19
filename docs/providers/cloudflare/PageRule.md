# Terraform::Cloudflare::PageRule

Provides a Cloudflare page rule resource.

## Properties

`Zone` - (Required) The DNS zone to which the page rule should be added.

`Target` - (Required) The URL pattern to target with the page rule.

`Actions` - (Required) The actions taken by the page rule, options given below.

`Priority` - (Optional) The priority of the page rule among others for this target, the higher the number the higher the priority as per [API documentation](https://api.cloudflare.com/#page-rules-for-a-zone-create-page-rule).

`Status` - (Optional) Whether the page rule is active or disabled.

`AlwaysOnline` - (Optional) Whether this action is `"on"` or `"off"`.

`AlwaysUseHttps` - (Optional) Boolean of whether this action is enabled. Default: false.

`AutomaticHttpsRewrites` - (Optional) Whether this action is `"on"` or `"off"`.

`BrowserCacheTtl` - (Optional) The Time To Live for the browser cache.

`BrowserCheck` - (Optional) Whether this action is `"on"` or `"off"`.

`CacheLevel` - (Optional) Whether to set the cache level to `"bypass"`, `"basic"`, `"simplified"`, `"aggressive"`, or `"cache_everything"`.

`DisableApps` - (Optional) Boolean of whether this action is enabled. Default: false.

`DisablePerformance` - (Optional) Boolean of whether this action is enabled. Default: false.

`DisableRailgun` - (Optional) Boolean of whether this action is enabled. Default: false.

`DisableSecurity` - (Optional) Boolean of whether this action is enabled. Default: false.

`EdgeCacheTtl` - (Optional) The Time To Live for the edge cache.

`EmailObfuscation` - (Optional) Whether this action is `"on"` or `"off"`.

`ExplicitCacheControl` - (Optional) Whether origin Cache-Control action is `"on"` or `"off"`.

`ForwardingUrl` - (Optional) The URL to forward to, and with what status. See below.

`HostHeaderOverride` - (Optional) Value of the Host header to send.

`IpGeolocation` - (Optional) Whether this action is `"on"` or `"off"`.

`Mirage` - (Optional) Whether this action is `"on"` or `"off"`.

`OpportunisticEncryption` - (Optional) Whether this action is `"on"` or `"off"`.

`Polish` - (Optional) Whether this action is `"off"`, `"lossless"` or `"lossy"`.

`ResolveOverride` - (Optional) Overridden origin server name.

`RocketLoader` - (Optional) Whether to set the rocket loader to `"on"`, `"off"`.

`SecurityLevel` - (Optional) Whether to set the security level to `"off"`, `"essentially_off"`, `"low"`, `"medium"`, `"high"`, or `"under_attack"`.

`ServerSideExclude` - (Optional) Whether this action is `"on"` or `"off"`.

`SmartErrors` - (Optional) Whether this action is `"on"` or `"off"`.

`Ssl` - (Optional) Whether to set the SSL mode to `"off"`, `"flexible"`, `"full"`, or `"strict"`.

`Waf` - (Optional) Whether this action is `"on"` or `"off"`.

`Url` - (Required) The URL to which the page rule should forward.

`StatusCode` - (Required) The status code to use for the redirection.


## Return Values

### Fn::GetAtt

`Id` - The page rule ID.

`ZoneId` - The ID of the zone in which the page rule will be applied.

`Target` - The URL pattern targeted by the page rule.

`Actions` - The actions applied by the page rule.

`Priority` - The priority of the page rule.

`Status` - Whether the page rule is active or disabled.

## See Also

* [cloudflare_page_rule](https://www.terraform.io/docs/providers/cloudflare/r/page_rule.html) in the _Terraform Provider Documentation_