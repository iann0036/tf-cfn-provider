# Terraform::Vault::JwtAuthBackend

Provides a resource for managing an
[JWT auth backend within Vault](https://www.vaultproject.io/docs/auth/jwt.html).

## Properties

`Path` - (Required) Path to mount the JWT auth backend.

`Description` - (Optional) The description of the auth backend.

`OidcDiscoveryUrl` - (Optional) The OIDC Discovery URL, without any .well-known component (base path). Cannot be used in combination with `JwtValidationPubkeys`.

`BoundIssuer` - (Optional) The value against which to match the iss claim in a JWT.

`OidcDiscoveryCaPem` - (Optional) The CA certificate or chain of certificates, in PEM format, to use to validate connections to the OIDC Discovery URL. If not set, system certificates are used.

`JwtValidationPubkeys` - (Optional) A list of PEM-encoded public keys to use to authenticate signatures locally. Cannot be used in combination with `OidcDiscoveryUrl`.


## See Also

* [vault_jwt_auth_backend](https://www.terraform.io/docs/providers/vault/r/jwt_auth_backend.html) in the _Terraform Provider Documentation_