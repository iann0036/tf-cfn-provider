# Terraform::OneAndOne::Server

Manages a Monitoring Policy on 1&1

## Properties

`Name` - (Required) The name of the VPN.

`Description` - (Optional) Description for the VPN.

`Email` - (Optional)  Email address to which notifications monitoring system will send.

`EmailNotification` - (Required) If set true email will be sent.

`Port` - (Required) Port number.

`Protocol` - (Required) The protocol of the port. Allowed values are `TCP`, `UDP`, `TCP/UDP`, `ICMP` and `IPSEC`.

`AlertIf` - (Required) Condition for the alert to be issued.

`Process` - (Required) Process name.


## See Also

* [oneandone_server](https://www.terraform.io/docs/providers/oneandone/r/server.html) in the _Terraform Provider Documentation_