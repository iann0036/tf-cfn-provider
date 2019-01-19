# Terraform::OCI::IdentityCustomerSecretKey

This resource provides the Customer Secret Key resource in Oracle Cloud Infrastructure Identity service.

Creates a new secret key for the specified user. Secret keys are used for authentication with the Object Storage Service's Amazon S3
compatible API. For information, see
[Managing User Credentials](https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcredentials.htm).

You must specify a *description* for the secret key (although it can be an empty string). It does not
have to be unique, and you can change it anytime with
[UpdateCustomerSecretKey](https://docs.cloud.oracle.com/iaas/api/#/en/identity/20160918/CustomerSecretKeySummary/UpdateCustomerSecretKey).

Every user has permission to create a secret key for *their own user ID*. An administrator in your organization
does not need to write a policy to give users this ability. To compare, administrators who have permission to the
tenancy can use this operation to create a secret key for any user, including themselves.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`DisplayName` - The display name you assign to the secret key. Does not have to be unique, and it's changeable.

`Id` - The OCID of the secret key.

`InactiveState` - The detailed status of INACTIVE lifecycleState.

`Key` - The secret key.

`State` - The secret key's current state.

`TimeCreated` - Date and time the `CustomerSecretKey` object was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

`TimeExpires` - Date and time when this password will expire, in the format defined by RFC3339. Null if it never expires.  Example: `2016-08-25T21:10:29.600Z`.

`UserId` - The OCID of the user the password belongs to.

## See Also

* [oci_identity_customer_secret_key](https://www.terraform.io/docs/providers/oci/r/identity_customer_secret_key.html) in the _Terraform Provider Documentation_