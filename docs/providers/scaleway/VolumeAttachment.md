# Terraform::Scaleway::VolumeAttachment

This allows volumes to be attached to servers.

~> **Warning:** Attaching volumes requires the servers to be powered off. This will lead to downtime if the server is already in use.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Id` - id of the new resource.

## See Also

* [scaleway_volume_attachment](https://www.terraform.io/docs/providers/scaleway/r/volume_attachment.html) in the _Terraform Provider Documentation_