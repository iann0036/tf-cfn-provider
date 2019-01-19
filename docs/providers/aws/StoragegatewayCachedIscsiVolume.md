# Terraform::AWS::StoragegatewayCachedIscsiVolume

Manages an AWS Storage Gateway cached iSCSI volume.

~> **NOTE:** The gateway must have cache added (e.g. via the [`aws_storagegateway_cache`](/docs/providers/aws/r/storagegateway_cache.html) resource) before creating volumes otherwise the Storage Gateway API will return an error.

~> **NOTE:** The gateway must have an upload buffer added (e.g. via the [`aws_storagegateway_upload_buffer`](/docs/providers/aws/r/storagegateway_upload_buffer.html) resource) before the volume is operational to clients, however the Storage Gateway API will allow volume creation without error in that case and return volume status as `UPLOAD BUFFER NOT CONFIGURED`.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

## See Also

* [aws_storagegateway_cached_iscsi_volume](https://www.terraform.io/docs/providers/aws/r/storagegateway_cached_iscsi_volume.html) in the _Terraform Provider Documentation_