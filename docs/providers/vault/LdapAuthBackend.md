# Terraform::Vault::LdapAuthBackend

Provides a resource for managing an [LDAP auth backend within Vault](https://www.vaultproject.io/docs/auth/ldap.html).

## Properties

`Url` - (Required) The URL of the LDAP server.

`Starttls` - (Optional) Control use of TLS when conecting to LDAP.

`TlsMinVersion` - (Optional) Minimum acceptable version of TLS.

`TlsMaxVersion` - (Optional) Maximum acceptable version of TLS.

`InsecureTls` - (Optional) Control whether or TLS certificates must be validated.

`Certificate` - (Optional) Trusted CA to validate TLS certificate.

`Binddn` - (Optional) DN of object to bind when performing user search.

`Bindpass` - (Optional) Password to use with `Binddn` when performing user search.

`Userdn` - (Optional) Base DN under which to perform user search.

`Userattr` - (Optional) Attribute on user object matching username passed in.

`Upndomain` - (Optional) The userPrincipalDomain used to construct UPN string.

`Groupfilter` - (Optional) Go template used to construct group membership query.

`Groupdn` - (Optional) Base DN under which to perform group search.

`Groupattr` - (Optional) LDAP attribute to follow on objects returned by groupfilter.

`Path` - (Optional) Path to mount the LDAP auth backend under.

`Description` - (Optional) Description for the LDAP auth backend mount.


## Return Values

### Fn::GetAtt

`Accessor` - The accessor for this auth mount.

## See Also

* [vault_ldap_auth_backend](https://www.terraform.io/docs/providers/vault/r/ldap_auth_backend.html) in the _Terraform Provider Documentation_