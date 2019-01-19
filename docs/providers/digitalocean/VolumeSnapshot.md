# Terraform::DigitalOcean::VolumeSnapshot

Provides a DigitalOcean Volume Snapshot which can be used to create a snapshot from an existing volume.

## Properties

`Name` - (Required) A name for the volume snapshot.

`VolumeId` - (Required) The ID of the volume from which the volume snapshot originated.


## Return Values

### Fn::GetAtt

`CreatedAt` - The date and time the volume snapshot was created.

`MinDiskSize` - The minimum size in gigabytes required for a volume to be created based on this volume snapshot.

`Regions` - A list of DigitalOcean region "slugs" indicating where the volume snapshot is available.

`Size` - The billable size of the volume snapshot in gigabytes.

## See Also

* [digitalocean_volume_snapshot](https://www.terraform.io/docs/providers/digitalocean/r/volume_snapshot.html) in the _Terraform Provider Documentation_