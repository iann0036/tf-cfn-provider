# Terraform::Vault::ApproleAuthBackendRole

Manages an AppRole auth backend role in a Vault server. See the [Vault
documentation](https://www.vaultproject.io/docs/auth/approle.html) for more
information.

## Properties

`RoleName` - (Required) The name of the role.

`RoleId` - (Optional) The RoleID of this role. If not specified, one will be
auto-generated.

`BindSecretId` - (Optional) Whether or not to require `secret_id` to be
presented when logging in using this AppRole. Defaults to `true`.

`BoundCidrList` - (Optional) If set, specifies blocks of IP addresses which
can perform the login operation.

`Policies` - (Optional) An array of strings specifying the policies to be set
on tokens issued using this role.

`SecretIdNumUses` - (Optional) The number of times any particular SecretID
can be used to fetch a token from this AppRole, after which the SecretID will
expire. A value of zero will allow unlimited uses.

`SecretIdTtl` - (Optional) The number of seconds after which any SecretID
expires.

`TokenNumUses` - (Optional) The number of times issued tokens can be used.
A value of 0 means unlimited uses.

`TokenTtl` - (Optional) The TTL period of tokens issued using this role,
provided as a number of seconds.

`TokenMaxTtl` - (Optional) The maximum allowed lifetime of tokens issued
using this role, provided as a number of seconds.

`Period` - (Optional) If set, indicates that the token generated using this
role should never expire. The token should be renewed within the duration
specified by this value. At each renewal, the token's TTL will be set to the
value of this field. The maximum allowed lifetime of token issued using this
role. Specified as a number of seconds.

`Backend` - (Optional) The unique name of the auth backend to configure.
Defaults to `approle`.


## See Also

* [vault_approle_auth_backend_role](https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role.html) in the _Terraform Provider Documentation_