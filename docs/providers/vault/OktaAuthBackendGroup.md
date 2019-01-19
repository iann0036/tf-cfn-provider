# Terraform::Vault::OktaAuthBackendGroup

Provides a resource to create a group in an
[Okta auth backend within Vault](https://www.vaultproject.io/docs/auth/okta.html).

## Properties

`Path` - (Required) The path where the Okta auth backend is mounted.

`GroupName` - (Required) Name of the group within the Okta.

`Policies` - (Optional) Vault policies to associate with this group.


## See Also

* [vault_okta_auth_backend_group](https://www.terraform.io/docs/providers/vault/r/okta_auth_backend_group.html) in the _Terraform Provider Documentation_