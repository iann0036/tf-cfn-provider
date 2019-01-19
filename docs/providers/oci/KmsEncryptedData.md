# Terraform::OCI::KmsEncryptedData

The `oci_kms_encrypted_data` resource creates and manages an OCI EncryptedData

Encrypts data using the given EncryptDataDetails resource. 
Plaintext included in the example request is a base64-encoded value 
of a UTF-8 string.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Ciphertext` - The encrypted data.

## See Also

* [oci_kms_encrypted_data](https://www.terraform.io/docs/providers/oci/r/kms_encrypted_data.html) in the _Terraform Provider Documentation_