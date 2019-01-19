# Terraform::DigitalOcean::FloatingIp

Provides a DigitalOcean Floating IP to represent a publicly-accessible static IP addresses that can be mapped to one of your Droplets.

~> **NOTE:** Floating IPs can be assigned to a Droplet either directly on the `Terraform::DigitalOcean::FloatingIp` resource by setting a `DropletId` or using the `digitaloceanFloatingIpAssignment` resource, but the two cannot be used together.

## Properties

`Region` - (Required) The region that the Floating IP is reserved to.

`DropletId` - (Optional) The ID of Droplet that the Floating IP will be assigned to.


## Return Values

### Fn::GetAtt

`IpAddress` - The IP Address of the resource.

## See Also

* [digitalocean_floating_ip](https://www.terraform.io/docs/providers/digitalocean/r/floating_ip.html) in the _Terraform Provider Documentation_