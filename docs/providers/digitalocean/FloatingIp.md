# Terraform::DigitalOcean::FloatingIp

Provides a DigitalOcean Floating IP to represent a publicly-accessible static IP addresses that can be mapped to one of your Droplets.

~> **NOTE:** Floating IPs can be assigned to a Droplet either directly on the `digitalocean_floating_ip` resource by setting a `droplet_id` or using the `digitalocean_floating_ip_assignment` resource, but the two cannot be used together.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`IpAddress` - The IP Address of the resource.

## See Also

* [digitalocean_floating_ip](https://www.terraform.io/docs/providers/digitalocean/r/floating_ip.html) in the _Terraform Provider Documentation_