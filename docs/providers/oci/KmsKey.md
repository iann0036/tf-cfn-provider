# Terraform::OCI::KmsKey

This resource provides the Key resource in Oracle Cloud Infrastructure Kms service.

Creates a new key.

## Properties

`CompartmentId` - (Required) The OCID of the compartment that contains this key.

`DesiredState` - (Optional) (Updatable) Desired state of the key. Possible values : `ENABLED` or `DISABLED`.

`DisplayName` - (Required) (Updatable) A user-friendly name for the key. It does not have to be unique, and it is changeable. Avoid entering confidential information.

`KeyShape` - (Required)
* `Algorithm` - (Required) The algorithm used by a key's KeyVersions to encrypt or decrypt.
* `Length` - (Required) The length of the key, expressed as an integer. Values of 16, 24, or 32 are supported.

`Algorithm` - (Required) The algorithm used by a key's KeyVersions to encrypt or decrypt.
* `Length` - (Required) The length of the key, expressed as an integer. Values of 16, 24, or 32 are supported.

`Length` - (Required) The length of the key, expressed as an integer. Values of 16, 24, or 32 are supported.

`ManagementEndpoint` - (Required) The service endpoint to perform management operations against. Management operations include 'Create,' 'Update,' 'List,' 'Get,' and 'Delete' operations. See Vault Management endpoint.


## Return Values

### Fn::GetAtt

`DisplayName` - A user-friendly name for the key. It does not have to be unique, and it is changeable. Avoid entering confidential information.

`CompartmentId` - The OCID of the compartment that contains this key.

`Algorithm` - The algorithm used by a key's KeyVersions to encrypt or decrypt.

`State` - The key's current state.  Example: `ENABLED`.

`TimeCreated` - The date and time the key was created, expressed in [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format.  Example: `2018-04-03T21:10:29.600Z`.

`Length` - The length of the key, expressed as an integer. Values of 16, 24, or 32 are supported.

`VaultId` - The OCID of the vault that contains this key.

`CurrentKeyVersion` - The OCID of the KeyVersion resource used in cryptographic operations. During key rotation, service may be in transitional state where this or a newer KeyVersion are used intermittently, and currentKeyVersion field is updated once service is guaranteed to use new KeyVersion for all consequent encrypt operations.

`Id` - The OCID of the key.

## See Also

* [oci_kms_key](https://www.terraform.io/docs/providers/oci/r/kms_key.html) in the _Terraform Provider Documentation_