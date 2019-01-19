# Terraform::OCI::IdentityUiPassword

This resource provides the Ui Password resource in Oracle Cloud Infrastructure Identity service.

Creates a new Console one-time password for the specified user. For more information about user
credentials, see [User Credentials](https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/usercredentials.htm).

Use this operation after creating a new user, or if a user forgets their password. The new one-time
password is returned to you in the response, and you must securely deliver it to the user. They'll
be prompted to change this password the next time they sign in to the Console. If they don't change
it within 7 days, the password will expire and you'll need to create a new one-time password for the
user.

**Note:** The user's Console login is the unique name you specified when you created the user
(see [CreateUser](https://docs.cloud.oracle.com/iaas/api/#/en/identity/20160918/User/CreateUser)).

## Return Values

### Fn::GetAtt

Fn::GetAtt returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

`InactiveStatus` - The detailed status of INACTIVE lifecycleState.

`Password` - The user's password for the Console.

`State` - The password's current state.

`TimeCreated` - Date and time the password was created, in the format defined by RFC3339.  Example: `2016-08-25T21:10:29.600Z`.

`UserId` - The OCID of the user.

## See Also

* [oci_identity_ui_password](https://www.terraform.io/docs/providers/oci/r/identity_ui_password.html) in the _Terraform Provider Documentation_