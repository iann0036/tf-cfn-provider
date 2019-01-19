# Terraform::BIGIP::LtmProfileFastl4

`Terraform::BIGIP::LtmProfileFastl4` Configures a custom profile_fastl4 for use by health checks.

For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

## Properties

`DefaultsFrom` - (Optional) Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.

`Partition` - (Optional) Displays the administrative partition within which this profile resides.

`ClientTimeout` - (Optional) Specifies late binding client timeout in seconds. This setting specifies the number of seconds allowed for a client to transmit enough data to select a server when late binding is enabled. If it expires timeout-recovery mode will dictate what action to take.

`ExplicitflowMigration` - (Optional) Enables or disables late binding explicit flow migration that allows iRules to control when flows move from software to hardware. Explicit flow migration is disabled by default hence BIG-IP automatically migrates flows from software to hardware.

`HardwareSyncookie` - (Optional) Enables or disables hardware SYN cookie support when PVA10 is present on the system. Note that when you set the hardware syncookie option to enabled, you may also want to set the following bigdb database variables using the "/sys modify db" command, based on your requirements: pva.SynCookies.Full.ConnectionThreshold (default: 500000), pva.SynCookies.Assist.ConnectionThreshold (default: 500000) pva.SynCookies.ClientWindow (default: 0). The default value is disabled.

`IdleTimeout` - (Optional) Specifies an idle timeout in seconds. This setting specifies the number of seconds that a connection is idle before the connection is eligible for deletion.When you specify an idle timeout for the Fast L4 profile, the value must be greater than the bigdb database variable Pva.Scrub time in msec for it to work properly.The default value is 300 seconds.

`IptosToclient` - (Optional) Specifies an IP ToS number for the client side. This option specifies the Type of Service level that the traffic management system assigns to IP packets when sending them to clients. The default value is 65535 (pass-through), which indicates, do not modify.

`IptosToserver` - (Optional) Specifies an IP ToS number for the server side. This setting specifies the Type of Service level that the traffic management system assigns to IP packets when sending them to servers. The default value is 65535 (pass-through), which indicates, do not modify.

`KeepaliveInterval` - (Optional) Specifies the keep alive probe interval, in seconds. The default value is disabled (0 seconds).


## See Also

* [bigip_ltm_profile_fastl4](https://www.terraform.io/docs/providers/bigip/r/ltm_profile_fastl4.html) in the _Terraform Provider Documentation_