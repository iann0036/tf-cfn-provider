# Terraform::NSXT::LbHttpApplicationProfile

Provides a resource to configure LB HTTP application profile on NSX-T manager

## Properties

`Description` - (Optional) Description of this resource.

`DisplayName` - (Optional) The display name of this resource. Defaults to ID if not set.

`HttpRedirectTo` - (Optional) A URL that incoming requests for that virtual server can be temporarily redirected to, If a website is temporarily down or has moved. When set, http_redirect_to_https should be false.

`HttpRedirectToHttps` - (Optional) A boolean flag which reflects whether the client will automatically be redirected to use SSL. When true, the http_redirect_to should not be specified.

`IdleTimeout` - (Optional) Timeout in seconds to specify how long an HTTP application can remain idle. Defaults to 15 seconds.

`Ntlm` - (Optional) A boolean flag which reflects whether NTLM challenge/response methodology will be used over HTTP. Can be set to true only if http_redirect_to_https is false.

`RequestBodySize` - (Optional) Maximum request body size in bytes. If it is not specified, it means that request body size is unlimited.

`RequestHeaderSize` - (Optional) Maximum request header size in bytes. Requests with larger header size will be processed as best effort whereas a request with header below this specified size is guaranteed to be processed. Defaults to 1024 bytes.

`ResponseTimeout` - (Optional) Number of seconds waiting for the server response before the connection is closed. Defaults to 60 seconds.

`XForwardedFor` - (Optional) When this value is set, the x_forwarded_for header in the incoming request will be inserted or replaced. Supported values are "INSERT" and "REPLACE".

`Tag` - (Optional) A list of scope + tag pairs to associate with this lb http profile.


## Return Values

### Fn::GetAtt

`Id` - ID of the lb http application profile.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

## See Also

* [nsxt_lb_http_application_profile](https://www.terraform.io/docs/providers/nsxt/r/lb_http_application_profile.html) in the _Terraform Provider Documentation_