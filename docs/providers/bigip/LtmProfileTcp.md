# Terraform::BIGIP::LtmProfileTcp

`Terraform::BIGIP::LtmProfileTcp` Configures a custom profile_tcp for use by health checks.

For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

## Properties

`Partition` - (Optional) Displays the administrative partition within which this profile resides.

`DefaultsFrom` - (Optional) Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.

`IdleTimeout` - (Optional) Specifies the number of seconds that a connection is idle before the connection is eligible for deletion. The default value is 300 seconds.

`CloseWaitTimeout` - (Optional) Specifies the number of seconds that a connection remains in a LAST-ACK state before quitting. A value of 0 represents a term of forever (or until the maxrtx of the FIN state). The default value is 5 seconds.

`FinwaitTimeout` - (Optional) Specifies the number of seconds that a connection is in the FIN-WAIT-1 or closing state before quitting. The default value is 5 seconds. A value of 0 (zero) represents a term of forever (or until the maxrtx of the FIN state). You can also specify immediate or indefinite.

`Finwait2timeout` - (Optional) Specifies the number of seconds that a connection is in the FIN-WAIT-2 state before quitting. The default value is 300 seconds. A value of 0 (zero) represents a term of forever (or until the maxrtx of the FIN state).

`KeepaliveInterval` - (Optional) Specifies the keep alive probe interval, in seconds. The default value is 1800 seconds.

`FastOpen` - (Optional) When enabled, permits TCP Fast Open, allowing properly equipped TCP clients to send data with the SYN packet.

`DeferredAccept` - (Optional) Specifies, when enabled, that the system defers allocation of the connection chain context until the client response is received. This option is useful for dealing with 3-way handshake DOS attacks. The default value is disabled.


## See Also

* [bigip_ltm_profile_tcp](https://www.terraform.io/docs/providers/bigip/r/ltm_profile_tcp.html) in the _Terraform Provider Documentation_