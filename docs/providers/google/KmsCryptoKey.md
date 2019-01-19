# Terraform::Google::KmsCryptoKey

Allows creation of a Google Cloud Platform KMS CryptoKey. For more information see
[the official documentation](https://cloud.google.com/kms/docs/object-hierarchy#key)
and
[API](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys).

A CryptoKey is an interface to key material which can be used to encrypt and decrypt data. A CryptoKey belongs to a
Google Cloud KMS KeyRing.

~> Note: CryptoKeys cannot be deleted from Google Cloud Platform. Destroying a
Terraform-managed CryptoKey will remove it from state and delete all
CryptoKeyVersions, rendering the key unusable, but **will not delete the
resource on the server**. When Terraform destroys these keys, any data
previously encrypted with these keys will be irrecoverable. For this reason, it
is strongly recommended that you add lifecycle hooks to the resource to prevent
accidental destruction.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`SelfLink` - The self link of the created CryptoKey. Its format is `projects/{projectId}/locations/{location}/keyRings/{keyRingName}/cryptoKeys/{cryptoKeyName}`.

## See Also

* [google_kms_crypto_key](https://www.terraform.io/docs/providers/google/r/kms_crypto_key.html) in the _Terraform Provider Documentation_