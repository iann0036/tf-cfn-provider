# Terraform::OCI::IdentityApiKey

This resource provides the Api Key resource in Oracle Cloud Infrastructure Identity service.

Uploads an API signing key for the specified user.

Every user has permission to use this operation to upload a key for *their own user ID*. An
administrator in your organization does not need to write a policy to give users this ability.
To compare, administrators who have permission to the tenancy can use this operation to upload a
key for any user, including themselves.

**Important:** Even though you have permission to upload an API key, you might not yet
have permission to do much else. If you try calling an operation unrelated to your own credential
management (e.g., `ListUsers`, `LaunchInstance`) and receive an "unauthorized" error,
check with an administrator to confirm which IAM Service group(s) you're in and what access
you have. Also confirm you're working in the correct compartment.

## Properties

`KeyValue` - (Required) The public key.  Must be an RSA key in PEM format.

`UserId` - (Required) The OCID of the user.


## Return Values

### Fn::GetAtt

`Fingerprint` - The key's fingerprint (e.g., 12:34:56:78:90:ab:cd:ef:12:34:56:78:90:ab:cd:ef).

`Id` - An Oracle-assigned identifier for the key, in this format: TENANCY_OCID/USER_OCID/KEY_FINGERPRINT.

`InactiveStatus` - The detailed status of INACTIVE lifecycleState.

`KeyValue` - The key's value.

`State` - The API key's current state.

`TimeCreated` - Date and time the `ApiKey` object was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

`UserId` - The OCID of the user the key belongs to.

## See Also

* [oci_identity_api_key](https://www.terraform.io/docs/providers/oci/r/identity_api_key.html) in the _Terraform Provider Documentation_