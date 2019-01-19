# Terraform::OCI::KmsKey

This resource provides the Key resource in Oracle Cloud Infrastructure Kms service.

Creates a new key.

## Properties

TBC

## Return Values

### Fn::GetAtt

`CompartmentId` - The OCID of the compartment that contains this key.

`CurrentKeyVersion` - The OCID of the KeyVersion resource used in cryptographic operations. During key rotation, service may be in transitional state where this or a newer KeyVersion are used intermittently, and currentKeyVersion field is updated once service is guaranteed to use new KeyVersion for all consequent encrypt operations.

`DisplayName` - A user-friendly name for the key. It does not have to be unique, and it is changeable. Avoid entering confidential information.

`Id` - The OCID of the key.

`Algorithm` - The algorithm used by a key's KeyVersions to encrypt or decrypt.

`Length` - The length of the key, expressed as an integer. Values of 16, 24, or 32 are supported.

`State` - The key's current state.  Example: `ENABLED`.

`TimeCreated` - The date and time the key was created, expressed in [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format.  Example: `2018-04-03T21:10:29.600Z`.

`VaultId` - The OCID of the vault that contains this key.

## See Also

* [oci_kms_key](https://www.terraform.io/docs/providers/oci/r/kms_key.html) in the _Terraform Provider Documentation_