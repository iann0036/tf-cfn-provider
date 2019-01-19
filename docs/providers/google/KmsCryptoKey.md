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

## Properties

`Name` - (Required) The CryptoKey's name. A CryptoKey’s name must be unique within a location and match the regular expression `[a-zA-Z0-9_-]{1,63}`.

`KeyRing` - (Required) The id of the Google Cloud Platform KeyRing to which the key shall belong.

`RotationPeriod` - (Optional) Every time this period passes, generate a new CryptoKeyVersion and set it as the primary. The first rotation will take place after the specified period. The rotation period has the format of a decimal number with up to 9 fractional digits, followed by the letter s (seconds). It must be greater than a day (ie, 86400).

`VersionTemplate` - (Optional) A template describing settings for new crypto key versions. Structure is documented below.

`Algorithm` - (Required)  The algorithm to use when creating a version based on this template. See the [algorithm reference](https://cloud.google.com/kms/docs/reference/rest/v1/CryptoKeyVersionAlgorithm) for possible inputs.

`ProtectionLevel` - (Optional) The protection level to use when creating a version based on this template. One of `SOFTWARE`, or `HSM`.


## Return Values

### Fn::GetAtt

`SelfLink` - The self link of the created CryptoKey. Its format is `projects/{projectId}/locations/{location}/keyRings/{keyRingName}/cryptoKeys/{cryptoKeyName}`.

## See Also

* [google_kms_crypto_key](https://www.terraform.io/docs/providers/google/r/kms_crypto_key.html) in the _Terraform Provider Documentation_