# Terraform::BIGIP::LtmProfileHttp2

`Terraform::BIGIP::LtmProfileHttp2` Configures a custom profile_http2 for use by health checks.

For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

## Properties

`DefaultsFrom` - (Required) Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.

`ConcurrentStreamsPerConnection` - (Optional) Specifies how many concurrent requests are allowed to be outstanding on a single HTTP/2 connection.

`ConnectionIdleTimeout` - (Optional) Specifies the number of seconds that a connection is idle before the connection is eligible for deletion..

`ConnpoolMaxsize` - (Optional) Specifies the maximum number of connections to a load balancing pool. A setting of 0 specifies that a pool can accept an unlimited number of connections. The default value is 2048.

`ActivationModes` - (Optional) Specifies what will cause an incoming connection to be handled as a HTTP/2 connection. The default values npn and alpn specify that the TLS next-protocol-negotiation and application-layer-protocol-negotiation extensions will be used.


## See Also

* [bigip_ltm_profile_http2](https://www.terraform.io/docs/providers/bigip/r/ltm_profile_http2.html) in the _Terraform Provider Documentation_