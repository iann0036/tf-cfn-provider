# Terraform::Scaleway::Volume

Provides volumes. This allows volumes to be created, updated and deleted.
For additional details please refer to [API documentation](https://developer.scaleway.com/#volumes).

## Properties

`Name` - (Required) name of volume.

`SizeInGb` - (Required) size of the volume in GB.

`Type` - (Required) type of volume.


## Return Values

### Fn::GetAtt

`Id` - id of the new resource.

`Server` - (Read Only) the `Terraform::Scaleway::Server` instance which has this volume mounted right now.

## See Also

* [scaleway_volume](https://www.terraform.io/docs/providers/scaleway/r/volume.html) in the _Terraform Provider Documentation_