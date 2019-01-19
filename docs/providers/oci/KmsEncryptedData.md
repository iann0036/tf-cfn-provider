# Terraform::OCI::KmsEncryptedData

The `Terraform::OCI::KmsEncryptedData` resource creates and manages an OCI EncryptedData

Encrypts data using the given EncryptDataDetails resource. 
Plaintext included in the example request is a base64-encoded value 
of a UTF-8 string.

## Properties

`AssociatedData` - (Optional) Information that can be used to provide an encryption context for the encrypted data. The length of the string representation of the associatedData must be fewer than 4096 characters.

`CryptoEndpoint` - (Required) The service endpoint to perform cryptographic operations against. Cryptographic operations include 'Encrypt,' 'Decrypt,' and 'GenerateDataEncryptionKey' operations. see Vault Crypto endpoint.

`KeyId` - (Required) The OCID of the key to encrypt with.

`Plaintext` - (Required) The plaintext data to encrypt.


## Return Values

### Fn::GetAtt

`Ciphertext` - The encrypted data.

## See Also

* [oci_kms_encrypted_data](https://www.terraform.io/docs/providers/oci/r/kms_encrypted_data.html) in the _Terraform Provider Documentation_