# Terraform::CloudScale::FloatingIp

Provides a cloudscale.ch Floating IP to represent a publicly-accessible static IP address or IP network that can be assigned to one of your cloudscale.ch servers. Floating IPs can be moved between servers. Possible use cases include: High-availability, non-disruptive maintenance, multiple IPs per server, or re-using the same IP after replacing a server.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Href` - The cloudscale.ch API URL of the current resource.

`Network` - The CIDR notation of the Floating IP address or network, e.g. `192.0.2.123/32`.

`NextHop` - The IP address of the server that your Floating IP is currently assigned to.

## See Also

* [cloudscale_floating_ip](https://www.terraform.io/docs/providers/cloudscale/r/floating_ip.html) in the _Terraform Provider Documentation_