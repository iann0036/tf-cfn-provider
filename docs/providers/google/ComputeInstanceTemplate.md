# Terraform::Google::ComputeInstanceTemplate

Manages a VM instance template resource within GCE. For more information see
[the official documentation](https://cloud.google.com/compute/docs/instance-templates)
and
[API](https://cloud.google.com/compute/docs/reference/latest/instanceTemplates).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`MetadataFingerprint` - The unique fingerprint of the metadata.

`SelfLink` - The URI of the created resource.

`TagsFingerprint` - The unique fingerprint of the tags.

## See Also

* [google_compute_instance_template](https://www.terraform.io/docs/providers/google/r/compute_instance_template.html) in the _Terraform Provider Documentation_