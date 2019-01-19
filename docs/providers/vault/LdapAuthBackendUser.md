# Terraform::Vault::LdapAuthBackendUser

Provides a resource to create a user in an [LDAP auth backend within Vault](https://www.vaultproject.io/docs/auth/ldap.html).

## Properties

`Username` - (Required) The LDAP username.

`Policies` - (Optional) Policies which should be granted to user.

`Groups` - (Optional) Override LDAP groups which should be granted to user.

`Backend` - (Optional) Path to the authentication backend.


## See Also

* [vault_ldap_auth_backend_user](https://www.terraform.io/docs/providers/vault/r/ldap_auth_backend_user.html) in the _Terraform Provider Documentation_