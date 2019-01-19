# Terraform::Google::ComputeInstance

Manages a VM instance resource within GCE. For more information see
[the official documentation](https://cloud.google.com/compute/docs/instances)
and
[API](https://cloud.google.com/compute/docs/reference/latest/instances).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`InstanceId` - The server-assigned unique identifier of this instance.

`MetadataFingerprint` - The unique fingerprint of the metadata.

`SelfLink` - The URI of the created resource.

`TagsFingerprint` - The unique fingerprint of the tags.

`LabelFingerprint` - The unique fingerprint of the labels.

`CpuPlatform` - The CPU platform used by this instance.

`NetworkInterface.0.networkIp` - The internal ip address of the instance, either manually or dynamically assigned.

`NetworkInterface.0.accessConfig.0.natIp` - If the instance has an access config, either the given external ip (in the `nat_ip` field) or the ephemeral (generated) ip (if you didn't provide one).

`AttachedDisk.0.diskEncryptionKeySha256` - The [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4).

`BootDisk.diskEncryptionKeySha256` - The [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4).

`Disk.0.diskEncryptionKeySha256` - The [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4).

## See Also

* [google_compute_instance](https://www.terraform.io/docs/providers/google/r/compute_instance.html) in the _Terraform Provider Documentation_