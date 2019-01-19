# Terraform::Google::KmsKeyRing

Allows creation of a Google Cloud Platform KMS KeyRing. For more information see
[the official documentation](https://cloud.google.com/kms/docs/object-hierarchy#key_ring)
and
[API](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings).

A KeyRing is a grouping of CryptoKeys for organizational purposes. A KeyRing belongs to a Google Cloud Platform Project
and resides in a specific location.

~> Note: KeyRings cannot be deleted from Google Cloud Platform. Destroying a Terraform-managed KeyRing will remove it
from state but **will not delete the resource on the server**.

## Properties

`Name` - (Required) The KeyRing's name. A KeyRing’s name must be unique within a location and match the regular expression `[a-zA-Z0-9_-]{1,63}`.

`Location` - (Required) The Google Cloud Platform location for the KeyRing. A full list of valid locations can be found by running `gcloud kms locations list`.

`Project` - (Optional) The project in which the resource belongs. If it is not provided, the provider project is used.


## Return Values

### Fn::GetAtt

`SelfLink` - The self link of the created KeyRing. Its format is `projects/{projectId}/locations/{location}/keyRings/{keyRingName}`.

## See Also

* [google_kms_key_ring](https://www.terraform.io/docs/providers/google/r/kms_key_ring.html) in the _Terraform Provider Documentation_