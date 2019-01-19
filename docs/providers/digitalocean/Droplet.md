# Terraform::DigitalOcean::Droplet

Provides a DigitalOcean Droplet resource. This can be used to create,
modify, and delete Droplets. Droplets also support
[provisioning](/docs/provisioners/index.html).

## Properties

`Image` - (Required) The Droplet image ID or slug.

`Name` - (Required) The Droplet name.

`Region` - (Required) The region to start in.

`Size` - (Required) The unique slug that indentifies the type of Droplet. You can find a list of available slugs on [DigitalOcean API documentation](https://developers.digitalocean.com/documentation/v2/#list-all-sizes).

`Backups` - (Optional) Boolean controlling if backups are made. Defaults to false.

`Monitoring` - (Optional) Boolean controlling whether monitoring agent is installed. Defaults to false.

`Ipv6` - (Optional) Boolean controlling if IPv6 is enabled. Defaults to false.

`PrivateNetworking` - (Optional) Boolean controlling if private networks are enabled. Defaults to false.

`SshKeys` - (Optional) A list of SSH IDs or fingerprints to enable in the format `[12345, 123456]`. To retrieve this info, use a tool such as `curl` with the [DigitalOcean API](https://developers.digitalocean.com/documentation/v2/#ssh-keys), to retrieve them.

`ResizeDisk` - (Optional) Boolean controlling whether to increase the disk size when resizing a Droplet. It defaults to `true`. When set to `false`, only the Droplet's RAM and CPU will be resized. **Increasing a Droplet's disk size is a permanent change**. Increasing only RAM and CPU is reversible.

`Tags` - (Optional) A list of the tags to label this Droplet. A tag resource must exist before it can be associated with a Droplet.


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