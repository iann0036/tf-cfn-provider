# Terraform::Alicloud::CdnDomain

Provides a CDN Accelerated Domain resource.

## Properties

`DomainName` - (Required) Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.

`CdnType` - (Required) Cdn type of the accelerated domain. Valid values are `web`, `download`, `video`, `liveStream`.

`SourceType` - (Optional) Source type of the accelerated domain. Valid values are `ipaddr`, `domain`, `oss`. You must set this parameter when `CdnType` value is not `liveStream`.

`SourcePort` - (Optional) Source port of the accelerated domain. Valid values are `80` and `443`. Default value is `80`. You must use `80` when the `SourceType` is `oss`.

`Sources` - (Optional, Type: list) Sources of the accelerated domain. It's a list of domain names or IP address and consists of at most 20 items. You must set this parameter when `CdnType` value is not `liveStream`.

`Scope` - (Optional) Scope of the accelerated domain. Valid values are `domestic`, `overseas`, `global`. Default value is `domestic`. This parameter's setting is valid Only for the international users and domestic L3 and above users .


## Return Values

### Fn::GetAtt

`DomainName` - The accelerated domain name.

`Sources` - The accelerated domain sources.

`CdnType` - The cdn type of the accelerated domain.

`SourceType` - The source type ot the accelerated domain.

`Scope` - The accelerated domain scope.

`OptimizeEnable` - The page optimize config of the accelerated domain.

`PageCompressEnable` - The page compress config of the accelerated domain.

`RangeEnable` - The range source config of the accelerated domain.

`VideoSeekEnable` - The video seek config of the accelerated domain.

`ParameterFilterConfig` - The parameter filter config of the accelerated domain.

`Page404Config` - The error page config of the accelerated domain.

`ReferConfig` - The refer config of the accelerated domain.

`AuthConfig` - The auth config of the accelerated domain.

`HttpHeaderConfig` - The http header configs of the accelerated domain.

`CacheConfig` - The cache configs of the accelerated domain.

## See Also

* [alicloud_cdn_domain](https://www.terraform.io/docs/providers/alicloud/r/cdn_domain.html) in the _Terraform Provider Documentation_