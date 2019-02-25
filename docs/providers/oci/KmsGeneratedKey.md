# Terraform::OCI::KmsGeneratedKey

The `Terraform::OCI::KmsGeneratedKey` resource creates and manages an OCI GeneratedKey

Generates a key that you can use to encrypt or decrypt data.

## Properties

`AssociatedData` - (Optional) Information that can be used to provide an encryption context for the  encrypted data. The length of the string representation of the associatedData must be fewer than 4096 characters.

`CryptoEndpoint` - (Required) The service endpoint to perform cryptographic operations against. Cryptographic operations include 'Encrypt,' 'Decrypt,' and 'GenerateDataEncryptionKey' operations. see Vault Crypto endpoint.

`IncludePlaintextKey` - (Required) If true, the generated key is also returned unencrypted.

`KeyId` - (Required) The OCID of the master encryption key to encrypt the generated data encryption key with.

`KeyShape` - (Required)
* `Algorithm` - (Required) The algorithm used by a key's KeyVersions to encrypt or decrypt.
* `Length` - (Required) The length of the key, expressed as an integer. Values of 16, 24, or 32 are supported.

`Algorithm` - (Required) The algorithm used by a key's KeyVersions to encrypt or decrypt.
* `Length` - (Required) The length of the key, expressed as an integer. Values of 16, 24, or 32 are supported.

`Length` - (Required) The length of the key, expressed as an integer. Values of 16, 24, or 32 are supported.


## Return Values

### Fn::GetAtt

`Plaintext` - The plaintext generated data encryption key, a base64-encoded sequence of random bytes, which is included if the  GenerateDataEncryptionKey request includes the "includePlaintextKey" parameter and sets its value to 'true'.

`Ciphertext` - The encrypted generated data encryption key.

`PlaintextChecksum` - The checksum of the plaintext generated data encryption key, which  is included if the GenerateDataEncryptionKey request includes the  "includePlaintextKey parameter and sets its value to 'true'.

## See Also

* [oci_kms_generated_key](https://www.terraform.io/docs/providers/oci/r/kms_generated_key.html) in the _Terraform Provider Documentation_