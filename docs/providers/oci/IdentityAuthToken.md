# Terraform::OCI::IdentityAuthToken

This resource provides the Auth Token resource in Oracle Cloud Infrastructure Identity service.

Creates a new auth token for the specified user. For information about what auth tokens are for, see
[Managing User Credentials](https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcredentials.htm).

You must specify a *description* for the auth token (although it can be an empty string). It does not
have to be unique, and you can change it anytime with
[UpdateAuthToken](https://docs.cloud.oracle.com/iaas/api/#/en/identity/20160918/AuthToken/UpdateAuthToken).

Every user has permission to create an auth token for *their own user ID*. An administrator in your organization
does not need to write a policy to give users this ability. To compare, administrators who have permission to the
tenancy can use this operation to create an auth token for any user, including themselves.

## Properties

`Description` - (Required) (Updatable) The description you assign to the auth token during creation. Does not have to be unique, and it's changeable.

`UserId` - (Required) The OCID of the user.


## Return Values

### Fn::GetAtt

`Description` - The description you assign to the auth token. Does not have to be unique, and it's changeable.

`Id` - The OCID of the auth token.

`InactiveState` - The detailed status of INACTIVE lifecycleState.

`State` - The token's current state.

`TimeCreated` - Date and time the `AuthToken` object was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

`TimeExpires` - Date and time when this auth token will expire, in the format defined by RFC3339. Null if it never expires.  Example: `2016-08-25T21:10:29.600Z`.

`Token` - The auth token. The value is available only in the response for `CreateAuthToken`, and not for `ListAuthTokens` or `UpdateAuthToken`.

`UserId` - The OCID of the user the auth token belongs to.

## See Also

* [oci_identity_auth_token](https://www.terraform.io/docs/providers/oci/r/identity_auth_token.html) in the _Terraform Provider Documentation_