# Terraform::BIGIP::LtmProfileFasthttp

`Terraform::BIGIP::LtmProfileFasthttp` Configures a custom profile_fasthttp for use by health checks.

For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

## Properties

`DefaultsFrom` - (Optional) Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.

`ConnpoolidleTimeoutoverride` - (Optional) Specifies the number of seconds after which a server-side connection in a OneConnect pool is eligible for deletion, when the connection has no traffic.The value of this option overrides the idle-timeout value that you specify. The default value is 0 (zero) seconds, which disables the override setting.

`ConnpoolMaxreuse` - (Optional) Specifies the maximum number of times that the system can re-use a current connection. The default value is 0 (zero).

`ConnpoolMaxsize` - (Optional) Specifies the maximum number of connections to a load balancing pool. A setting of 0 specifies that a pool can accept an unlimited number of connections. The default value is 2048.

`ConnpoolReplenish` - (Optional) The default value is enabled. When this option is enabled, the system replenishes the number of connections to a load balancing pool to the number of connections that existed when the server closed the connection to the pool. When disabled, the system replenishes the connection that was closed by the server, only when there are fewer connections to the pool than the number of connections set in the connpool-min-size connections option. Also see the connpool-min-size option..

`IdleTimeout` - (Optional) Specifies an idle timeout in seconds. This setting specifies the number of seconds that a connection is idle before the connection is eligible for deletion.When you specify an idle timeout for the Fast L4 profile, the value must be greater than the bigdb database variable Pva.Scrub time in msec for it to work properly.The default value is 300 seconds.

`ConnpoolMinsize` - (Optional) Specifies the minimum number of connections to a load balancing pool. A setting of 0 specifies that there is no minimum. The default value is 10.

`ConnpoolStep` - (Optional) Specifies the increment in which the system makes additional connections available, when all available connections are in use. The default value is 4.

`Forcehttp10response` - (Optional) Specifies whether to rewrite the HTTP version in the status line of the server to HTTP 1.0 to discourage the client from pipelining or chunking data. The default value is disabled.

`MaxheaderSize` - (Optional) Specifies the maximum amount of HTTP header data that the system buffers before making a load balancing decision. The default setting is 32768.


## See Also

* [bigip_ltm_profile_fasthttp](https://www.terraform.io/docs/providers/bigip/r/ltm_profile_fasthttp.html) in the _Terraform Provider Documentation_