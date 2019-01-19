# Terraform::BIGIP::LtmProfileOneconnect

`Terraform::BIGIP::LtmProfileOneconnect` Configures a custom profile_oneconnect for use by health checks.

For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

## Properties

`Partition` - (Optional) Displays the administrative partition within which this profile resides.

`DefaultsFrom` - (Optional) Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.

`IdleTimeoutOverride` - (Optional) Specifies the number of seconds that a connection is idle before the connection flow is eligible for deletion. Possible values are disabled, indefinite, or a numeric value that you specify. The default value is disabled.

`SharePools` - (Optional) Specify if you want to share the pool, default value is "disabled".

`MaxAge` - (Optional) Specifies the maximum age in number of seconds allowed for a connection in the connection reuse pool. For any connection with an age higher than this value, the system removes that connection from the reuse pool. The default value is 86400.

`MaxReuse` - (Optional) Specifies the maximum number of times that a server-side connection can be reused. The default value is 1000.

`MaxSize` - (Optional) Specifies the maximum number of connections that the system holds in the connection reuse pool. If the pool is already full, then the server-side connection closes after the response is completed. The default value is 10000.

`SourceMask` - (Optional) Specifies a source IP mask. The default value is 0.0.0.0. The system applies the value of this option to the source address to determine its eligibility for reuse. A mask of 0.0.0.0 causes the system to share reused connections across all clients. A host mask (all 1's in binary), causes the system to share only those reused connections originating from the same client IP address.


## See Also

* [bigip_ltm_profile_oneconnect](https://www.terraform.io/docs/providers/bigip/r/ltm_profile_oneconnect.html) in the _Terraform Provider Documentation_