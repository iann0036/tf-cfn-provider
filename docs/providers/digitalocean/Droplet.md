# Terraform::DigitalOcean::Droplet

Provides a DigitalOcean Droplet resource. This can be used to create,
modify, and delete Droplets. Droplets also support
[provisioning](/docs/provisioners/index.html).

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The ID of the Droplet.

`Name` - The name of the Droplet.

`Region` - The region of the Droplet.

`Image` - The image of the Droplet.

`Ipv6` - Is IPv6 enabled.

`Ipv6Address` - The IPv6 address.

`Ipv6AddressPrivate` - The private networking IPv6 address.

`Ipv4Address` - The IPv4 address.

`Ipv4AddressPrivate` - The private networking IPv4 address.

`Locked` - Is the Droplet locked.

`PrivateNetworking` - Is private networking enabled.

`PriceHourly` - Droplet hourly price.

`PriceMonthly` - Droplet monthly price.

`Size` - The instance size.

`Disk` - The size of the instance's disk in GB.

`Vcpus` - The number of the instance's virtual CPUs.

`Status` - The status of the Droplet.

`Tags` - The tags associated with the Droplet.

`VolumeIds` - A list of the attached block storage volumes.

## See Also

* [digitalocean_droplet](https://www.terraform.io/docs/providers/digitalocean/r/droplet.html) in the _Terraform Provider Documentation_