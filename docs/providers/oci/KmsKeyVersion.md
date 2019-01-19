# Terraform::OCI::KmsKeyVersion

The `oci_kms_key_version` resource creates and manages an OCI KeyVersion

Generates new cryptographic material for a key. Key must be in an `ENABLED` state to be
rotated.

## Properties

TBC

## Return Values

### Fn::GetAtt

`CompartmentId` - The OCID of the compartment that contains this key version.

`Id` - The OCID of the key version.

`KeyId` - The OCID of the key associated with this key version.

`TimeCreated` - The date and time this key version was created, expressed in [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format.  Example: `2018-04-03T21:10:29.600Z`.

`VaultId` - The OCID of the vault that contains this key version.

## See Also

* [oci_kms_key_version](https://www.terraform.io/docs/providers/oci/r/kms_key_version.html) in the _Terraform Provider Documentation_