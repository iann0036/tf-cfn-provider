# Terraform::Vault::OktaAuthBackendUser

Provides a resource to create a user in an
[Okta auth backend within Vault](https://www.vaultproject.io/docs/auth/okta.html).

## Properties

`Path` - (Required) The path where the Okta auth backend is mounted.

`Username` - (Required Optional) Name of the user within Okta.

`Groups` - (Optional) List of Okta groups to associate with this user.

`Policies` - (Optional) List of Vault policies to associate with this user.


## See Also

* [vault_okta_auth_backend_user](https://www.terraform.io/docs/providers/vault/r/okta_auth_backend_user.html) in the _Terraform Provider Documentation_