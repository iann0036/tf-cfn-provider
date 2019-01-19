# Terraform::DigitalOcean::DropletSnapshot

Provides a resource which can be used to create a snapshot from an existing DigitalOcean Droplet.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`CreatedAt` - The date and time the Droplet snapshot was created.

`MinDiskSize` - The minimum size in gigabytes required for a Droplet to be created based on this snapshot.

`Regions` - A list of DigitalOcean region "slugs" indicating where the droplet snapshot is available.

`Size` - The billable size of the Droplet snapshot in gigabytes.

## See Also

* [digitalocean_droplet_snapshot](https://www.terraform.io/docs/providers/digitalocean/r/droplet_snapshot.html) in the _Terraform Provider Documentation_