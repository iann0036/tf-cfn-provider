# Terraform::HCloud::FloatingIp

Provides a Hetzner Cloud Floating IP to represent a publicly-accessible static IP address that can be mapped to one of your servers.

## Properties

`Type` - (Required, string) Type of the Floating IP. `ipv4` `ipv6` - `ServerId` - (Optional, int) Server to assign the Floating IP to. - `HomeLocation` - (Optional, string) Home location (routing is optimized for that location). Optional if server_id argument is passed. - `Description` - (Optional, string) Description of the Floating IP.

`ServerId` - (Optional, int) Server to assign the Floating IP to. - `HomeLocation` - (Optional, string) Home location (routing is optimized for that location). Optional if server_id argument is passed. - `Description` - (Optional, string) Description of the Floating IP.

`HomeLocation` - (Optional, string) Home location (routing is optimized for that location). Optional if server_id argument is passed. - `Description` - (Optional, string) Description of the Floating IP.

`Description` - (Optional, string) Description of the Floating IP.


## See Also

* [hcloud_floating_ip](https://www.terraform.io/docs/providers/hcloud/r/floating_ip.html) in the _Terraform Provider Documentation_