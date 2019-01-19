# Terraform::Vault::LdapAuthBackendGroup

Provides a resource to create a group in an [LDAP auth backend within Vault](https://www.vaultproject.io/docs/auth/ldap.html).

## Properties

`Groupname` - (Required) The LDAP groupname.

`Policies` - (Optional) Policies which should be granted to members of the group.

`Backend` - (Optional) Path to the authentication backend.


## See Also

* [vault_ldap_auth_backend_group](https://www.terraform.io/docs/providers/vault/r/ldap_auth_backend_group.html) in the _Terraform Provider Documentation_