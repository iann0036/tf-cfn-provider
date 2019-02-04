# Terraform::Vault::JwtAuthBackendRole

Manages an JWT auth backend role in a Vault server. See the [Vault
documentation](https://www.vaultproject.io/docs/auth/jwt.html) for more
information.

## Properties

`RoleName` - (Required) The name of the role.

`BoundAudiences` - (Required) List of `aud` claims to match
against. Any match is sufficient.

`UserClaim` - (Required) The claim to use to uniquely identify
the user; this will be used as the name for the Identity entity alias created
due to a successful login.

`Policies` - (Optional) Policies to be set on tokens issued using this role.

`Ttl` - (Optional) The initial/renewal TTL of tokens issued using this role,
in seconds.

`MaxTtl` - (Optional) The maximum allowed lifetime of tokens issued using
this role, in seconds.

`Period` - (Optional) If set, indicates that the token generated
using this role should never expire, but instead always use the value set
here as the TTL for every renewal.

`NumUses` - (Optional) If set, puts a use-count limitation on the issued
token.

`BoundSubject` - (Optional) If set, requires that the `sub` claim matches
this value.

`BoundCidrs` - (Optional) If set, a list of CIDRs valid as the source
address for login requests. This value is also encoded into any resulting
token.

`GroupsClaim` - (Optional) The claim to use to uniquely identify
the set of groups to which the user belongs; this will be used as the names
for the Identity group aliases created due to a successful login. The claim
value must be a list of strings.

`Backend` - (Optional) The unique name of the auth backend to configure.
Defaults to `jwt`.


## See Also

* [vault_jwt_auth_backend_role](https://www.terraform.io/docs/providers/vault/r/jwt_auth_backend_role.html) in the _Terraform Provider Documentation_