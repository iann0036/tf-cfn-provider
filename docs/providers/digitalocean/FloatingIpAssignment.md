# Terraform::DigitalOcean::FloatingIpAssignment

Provides a resource for assigning an existing DigitalOcean Floating IP to a Droplet. This
makes it easy to provision floating IP addresses that are not tied to the lifecycle of your
Droplet.

## Properties

`IpAddress` - (Required) The Floating IP to assign to the Droplet.

`DropletId` - (Optional) The ID of Droplet that the Floating IP will be assigned to.


## See Also

* [digitalocean_floating_ip_assignment](https://www.terraform.io/docs/providers/digitalocean/r/floating_ip_assignment.html) in the _Terraform Provider Documentation_