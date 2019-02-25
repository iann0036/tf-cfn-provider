# Terraform::AzureAD::User

Manages a User within Azure Active Directory.

-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to `Directory.ReadWrite.All` within the `Windows Azure Active Directory` API.

## Properties

`UserPrincipalName` - (Required) The User Principal Name of the Azure AD User.

`DisplayName` - (Required) The name to display in the address book for the user.

`MailNickname` - (Required) The mail alias for the user.

`AccountEnabled` - (Optional) `true` if the account should be enabled, otherwise `false`. Defaults to `true`.

`Password` - (Required) The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 16 characters.

`ForcePasswordChange` - (Optional) `true` if the User is forced to change the password during the next sign-in. Defaults to `false`.


## Return Values

### Fn::GetAtt

`Id` - The Object ID of the Azure AD User.

`Mail` - The primary email address of the Azure AD User.

## See Also

* [azuread_user](https://www.terraform.io/docs/providers/azuread/r/user.html) in the _Terraform Provider Documentation_