# Terraform::BIGIP::LtmMonitor

`Terraform::BIGIP::LtmMonitor` Configures a custom monitor for use by health checks.

For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

## Properties

`Parent` - (Required) Existing LTM monitor to inherit from.

`Interval` - (Optional) Check interval in seconds.

`Timeout` - (Optional) Timeout in seconds.

`Send` - (Optional) Request string to send.

`Receive` - (Optional) Expected response string.

`ReceiveDisable` - (Optional).

`Reverse` - (Optional).

`Transparent` - (Optional).

`ManualResume` - (Optional).

`IpDscp` - (Optional).

`TimeUntilUp` - (Optional).

`Destination` - (Optional) Specify an alias address for monitoring.

`Compatibility` -  (Optional) Specifies, when enabled, that the SSL options setting (in OpenSSL) is set to ALL. Accepts 'enabled' or 'disabled' values, the default value is 'enabled'.

`Filename` - (Optional) Specifies the full path and file name of the file that the system attempts to download. The health check is successful if the system can download the file.

`Mode` - (Optional) Specifies the data transfer process (DTP) mode. The default value is passive. The options are passive (Specifies that the monitor sends a data transfer request to the FTP server. When the FTP server receives the request, the FTP server then initiates and establishes the data connection.) and active (Specifies that the monitor initiates and establishes the data connection with the FTP server.).


## See Also

* [bigip_ltm_monitor](https://www.terraform.io/docs/providers/bigip/r/ltm_monitor.html) in the _Terraform Provider Documentation_