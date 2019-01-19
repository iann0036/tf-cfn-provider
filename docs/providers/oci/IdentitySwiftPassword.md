# Terraform::OCI::IdentitySwiftPassword

This resource provides the Swift Password resource in Oracle Cloud Infrastructure Identity service.

**Deprecated. Use [CreateAuthToken](https://docs.cloud.oracle.com/iaas/api/#/en/identity/20160918/AuthToken/CreateAuthToken) instead.**

Creates a new Swift password for the specified user. For information about what Swift passwords are for, see
[Managing User Credentials](https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcredentials.htm).

You must specify a *description* for the Swift password (although it can be an empty string). It does not
have to be unique, and you can change it anytime with
[UpdateSwiftPassword](https://docs.cloud.oracle.com/iaas/api/#/en/identity/20160918/SwiftPassword/UpdateSwiftPassword).

Every user has permission to create a Swift password for *their own user ID*. An administrator in your organization
does not need to write a policy to give users this ability. To compare, administrators who have permission to the
tenancy can use this operation to create a Swift password for any user, including themselves.

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`Description` - The description you assign to the Swift password. Does not have to be unique, and it's changeable.

`ExpiresOn` - Date and time when this password will expire, in the format defined by RFC3339. Null if it never expires.  Example: `2016-08-25T21:10:29.600Z`.

`Id` - The OCID of the Swift password.

`InactiveState` - The detailed status of INACTIVE lifecycleState.

`Password` - The Swift password. The value is available only in the response for `CreateSwiftPassword`, and not for `ListSwiftPasswords` or `UpdateSwiftPassword`.

`State` - The password's current state.

`TimeCreated` - Date and time the `SwiftPassword` object was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

`UserId` - The OCID of the user the password belongs to.

## See Also

* [oci_identity_swift_password](https://www.terraform.io/docs/providers/oci/r/identity_swift_password.html) in the _Terraform Provider Documentation_