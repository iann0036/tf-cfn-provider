# Terraform::AWS::StoragegatewayCachedIscsiVolume

Manages an AWS Storage Gateway cached iSCSI volume.

~> **NOTE:** The gateway must have cache added (e.g. via the [`Terraform::AWS::StoragegatewayCache`](/docs/providers/aws/r/storagegateway_cache.html) resource) before creating volumes otherwise the Storage Gateway API will return an error.

~> **NOTE:** The gateway must have an upload buffer added (e.g. via the [`Terraform::AWS::StoragegatewayUploadBuffer`](/docs/providers/aws/r/storagegatewayUploadBuffer.html) resource) before the volume is operational to clients, however the Storage Gateway API will allow volume creation without error in that case and return volume status as `UPLOAD BUFFER NOT CONFIGURED`.

## Properties

`GatewayArn` - (Required) The Amazon Resource Name (ARN) of the gateway.

`NetworkInterfaceId` - (Required) The network interface of the gateway on which to expose the iSCSI target. Only IPv4 addresses are accepted.

`TargetName` - (Required) The name of the iSCSI target used by initiators to connect to the target and as a suffix for the target ARN. The target name must be unique across all volumes of a gateway.

`VolumeSizeInBytes` - (Required) The size of the volume in bytes.

`SnapshotId` - (Optional) The snapshot ID of the snapshot to restore as the new cached volume. e.g. `snap-1122aabb`.

`SourceVolumeArn` - (Optional) The ARN for an existing volume. Specifying this ARN makes the new volume into an exact copy of the specified existing volume's latest recovery point. The `VolumeSizeInBytes` value for this new volume must be equal to or larger than the size of the existing volume, in bytes.


## See Also

* [aws_storagegateway_cached_iscsi_volume](https://www.terraform.io/docs/providers/aws/r/storagegateway_cached_iscsi_volume.html) in the _Terraform Provider Documentation_