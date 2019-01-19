# Terraform::Scaleway::Volume

Provides volumes. This allows volumes to be created, updated and deleted.
For additional details please refer to [API documentation](https://developer.scaleway.com/#volumes).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - id of the new resource.

`Server` - (Read Only) the `scaleway_server` instance which has this volume mounted right now.

## See Also

* [scaleway_volume](https://www.terraform.io/docs/providers/scaleway/r/volume.html) in the _Terraform Provider Documentation_