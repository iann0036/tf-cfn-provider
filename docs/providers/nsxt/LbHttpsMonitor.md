# Terraform::NSXT::LbHttpsMonitor

Provides a resource to configure lb https monitor on NSX-T manager

## Properties

`Description` - (Optional) Description of this resource.

`DisplayName` - (Optional) The display name of this resource. Defaults to ID if not set.

`Tag` - (Optional) A list of scope + tag pairs to associate with this lb https monitor.

`FallCount` - (Optional) Number of consecutive checks that must fail before marking it down.

`Interval` - (Optional) The frequency at which the system issues the monitor check (in seconds).

`MonitorPort` - (Optional) If the monitor port is specified, it would override pool member port setting for healthcheck. A port range is not supported.

`RiseCount` - (Optional) Number of consecutive checks that must pass before marking it up.

`Timeout` - (Optional) Number of seconds the target has to respond to the monitor request.

`CertificateChainDepth` - (Optional) Authentication depth is used to set the verification depth in the server certificates chain.

`Ciphers` - (Optional) List of supported SSL ciphers.

`ClientCertificateId` - (Optional) Client certificate can be specified to support client authentication.

`Protocols` - (Optional) SSL versions TLS1.1 and TLS1.2 are supported and enabled by default. SSLv2, SSLv3, and TLS1.0 are supported, but disabled by default.

`RequestBody` - (Optional) String to send as HTTP health check request body. Valid only for certain HTTP methods like POST.

`RequestHeader` - (Optional) HTTP request headers.

`RequestMethod` - (Optional) Health check method for HTTP monitor type. Valid values are GET, HEAD, PUT, POST and OPTIONS.

`RequestUrl` - (Optional) URL used for HTTP monitor.

`RequestVersion` - (Optional) HTTP request version. Valid values are HTTP_VERSION_1_0 and HTTP_VERSION_1_1.

`ResponseBody` - (Optional) If response body is specified, healthcheck HTTP response body is matched against the specified string and server is considered healthy only if there is a match (regular expressions not supported). If response body string is not specified, HTTP healthcheck is considered successful if the HTTP response status code is among configured values.

`ResponseStatusCodes` - (Optional) HTTP response status code should be a valid HTTP status code.

`ServerAuth` - (Optional) Server authentication mode - REQUIRED or IGNORE.

`ServerAuthCaIds` - (Optional) If server auth type is REQUIRED, server certificate must be signed by one of the trusted Certificate Authorities (CAs), also referred to as root CAs, whose self signed certificates are specified.

`ServerAuthCrlIds` - (Optional) A Certificate Revocation List (CRL) can be specified in the server-side SSL profile binding to disallow compromised server certificates.


## Return Values

### Fn::GetAtt

`Id` - ID of the lb_https_monitor.

`Revision` - Indicates current revision number of the object as seen by NSX-T API server. This attribute can be useful for debugging.

`IsSecure` - This flag is set to true when all the ciphers and protocols are secure. It is set to false when one of the ciphers or protocols is insecure.

## See Also

* [nsxt_lb_https_monitor](https://www.terraform.io/docs/providers/nsxt/r/lb_https_monitor.html) in the _Terraform Provider Documentation_