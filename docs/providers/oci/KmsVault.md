# Terraform::OCI::KmsVault

The `Terraform::OCI::KmsVault` resource creates and manages an OCI Vault

Creates a new vault. The type of vault you create determines key 
placement, pricing, and available options. Options include storage 
isolation, a dedicated service endpoint instead of a shared service
endpoint for API calls, and a dedicated HSM or a multitenant HSM.

## Properties

`CompartmentId` - (Required) The OCID of the compartment where you want to create this vault.

`DisplayName` - (Required) (Updatable) A user-friendly name for the vault. It does not have to be unique, and it is changeable. Avoid entering confidential information.

`VaultType` - (Required) The type of vault to create. Each type of vault stores the key with different degrees of isolation and has different options and pricing.


## Return Values

### Fn::GetAtt

`DisplayName` - A user-friendly name for the vault. It does not have to be unique, and it is changeable. Avoid entering confidential information.

`CompartmentId` - The OCID of the compartment that contains this vault.

`VaultType` - The type of vault. Each type of vault stores the key with different degrees of isolation and has different options and pricing.

`CryptoEndpoint` - The service endpoint to perform cryptographic operations against. Cryptographic operations include 'Encrypt,' 'Decrypt,' and 'GenerateDataEncryptionKey' operations.

`TimeOfDeletion` - An optional property for the deletion time of the Vault expressed in [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format. Example: `2018-04-03T21:10:29.600Z`.

`TimeCreated` - The date and time this vault was created, expressed in [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp format.  Example: `2018-04-03T21:10:29.600Z`.

`State` - The vault's current state.  Example: `DELETED`.

`ManagementEndpoint` - The service endpoint to perform management operations against. Management operations include 'Create,' 'Update,' 'List,' 'Get,' and 'Delete' operations.

`Id` - The OCID of the vault.

## See Also

* [oci_kms_vault](https://www.terraform.io/docs/providers/oci/r/kms_vault.html) in the _Terraform Provider Documentation_