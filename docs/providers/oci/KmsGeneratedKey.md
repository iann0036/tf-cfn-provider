# Terraform::OCI::KmsGeneratedKey

The `oci_kms_generated_key` resource creates and manages an OCI GeneratedKey

Generates a key that you can use to encrypt or decrypt data.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Ciphertext` - The encrypted generated data encryption key.

`Plaintext` - The plaintext generated data encryption key, a base64-encoded sequence of random bytes, which is included if the  GenerateDataEncryptionKey request includes the "includePlaintextKey" parameter and sets its value to 'true'.

`PlaintextChecksum` - The checksum of the plaintext generated data encryption key, which  is included if the GenerateDataEncryptionKey request includes the  "includePlaintextKey parameter and sets its value to 'true'.

## See Also

* [oci_kms_generated_key](https://www.terraform.io/docs/providers/oci/r/kms_generated_key.html) in the _Terraform Provider Documentation_