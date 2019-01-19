# Terraform::AzureRM::CdnEndpoint

A CDN Endpoint is the entity within a CDN Profile containing configuration information regarding caching behaviors and origins. The CDN Endpoint is exposed using the URL format <endpointname>.azureedge.net.

## Properties

`Name` - (Required) Specifies the name of the CDN Endpoint. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the CDN Endpoint.

`ProfileName` - (Required) The CDN Profile to which to attach the CDN Endpoint.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`IsHttpAllowed` - (Optional) Defaults to `true`.

`IsHttpsAllowed` - (Optional) Defaults to `true`.

`ContentTypesToCompress` - (Optional) An array of strings that indicates a content types on which compression will be applied. The value for the elements should be MIME types.

`GeoFilter` - (Optional) A set of Geo Filters for this CDN Endpoint. Each `GeoFilter` block supports fields documented below.

`IsCompressionEnabled` - (Optional) Indicates whether compression is to be enabled. Defaults to false.

`QuerystringCachingBehaviour` - (Optional) Sets query string caching behavior. Allowed values are `IgnoreQueryString`, `BypassCaching` and `UseQueryString`. Defaults to `IgnoreQueryString`.

`OptimizationType` - (Optional) What types of optimization should this CDN Endpoint optimize for? Possible values include `DynamicSiteAcceleration`, `GeneralMediaStreaming`, `GeneralWebDelivery`, `LargeFileDownload` and `VideoOnDemandMediaStreaming`.

`Origin` - (Optional) The set of origins of the CDN endpoint. When multiple origins exist, the first origin will be used as primary and rest will be used as failover options. Each `Origin` block supports fields documented below.

`OriginHostHeader` - (Optional) The host header CDN provider will send along with content requests to origins. Defaults to the host name of the origin.

`OriginPath` - (Optional) The path used at for origin requests.

`ProbePath` - (Optional) the path to a file hosted on the origin which helps accelerate delivery of the dynamic content and calculate the most optimal routes for the CDN. This is relative to the `OriginPath`.

`Tags` - (Optional) A mapping of tags to assign to the resource.

### Origin Properties

`Name` - (Required) The name of the origin. This is an arbitrary value. However, this value needs to be unique under the endpoint. Changing this forces a new resource to be created.

`HostName` - (Required) A string that determines the hostname/IP address of the origin server. This string can be a domain name, Storage Account endpoint, Web App endpoint, IPv4 address or IPv6 address. Changing this forces a new resource to be created.

`HttpPort` - (Optional) The HTTP port of the origin. Defaults to `80`. Changing this forces a new resource to be created.

`HttpsPort` - (Optional) The HTTPS port of the origin. Defaults to `443`. Changing this forces a new resource to be created.

### GeoFilter Properties

`RelativePath` - (Required) The relative path applicable to geo filter.

`Action` - (Required) The Action of the Geo Filter. Possible values include `Allow` and `Block`.

`CountryCodes` - (Required) A List of two letter country codes (e.g. `US`, `GB`) to be associated with this Geo Filter.


## Return Values

### Fn::GetAtt

`Id` - The CDN Endpoint ID.

## See Also

* [azurerm_cdn_endpoint](https://www.terraform.io/docs/providers/azurerm/r/cdn_endpoint.html) in the _Terraform Provider Documentation_