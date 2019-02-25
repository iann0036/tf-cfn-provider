# Terraform::OCI::IdentityUser

This resource provides the User Capabilities Management resource in Oracle Cloud Infrastructure Identity service.

Manages the capabilities of the specified user.

**Important:** Deleting the User Capabilities Management leaves the User resource in its existing state (rather than returning to its defaults)

## Properties

`UserId` - (Required) The OCID of the user.

`CanUseApiKeys` - (Optional) (Updatable) Indicates if the user can use API keys.

`CanUseAuthTokens` - (Optional) (Updatable) Indicates if the user can use SWIFT passwords / auth tokens.

`CanUseConsolePassword` - (Optional) (Updatable) Indicates if the user can log in to the console.

`CanUseCustomerSecretKeys` - (Optional) (Updatable) Indicates if the user can use SigV4 symmetric keys.

`CanUseSmtpCredentials` - (Optional) (Updatable) Indicates if the user can use SMTP passwords.


## Return Values

### Fn::GetAtt

`CanUseConsolePassword` - Indicates if the user can log in to the console.

`CanUseApiKeys` - Indicates if the user can use API keys.

`CanUseAuthTokens` - Indicates if the user can use SWIFT passwords / auth tokens.

`UserId` - The OCID of the user.

`CanUseSmtpCredentials` - Indicates if the user can use SMTP passwords.

`CanUseCustomerSecretKeys` - Indicates if the user can use SigV4 symmetric keys.

## See Also

* [oci_identity_user](https://www.terraform.io/docs/providers/oci/r/identity_user.html) in the _Terraform Provider Documentation_