# Terraform::Vault::ApproleAuthBackendRoleSecretId

Manages an AppRole auth backend SecretID in a Vault server. See the [Vault
documentation](https://www.vaultproject.io/docs/auth/approle.html) for more
information.

## Properties

`RoleName` - (Required) The name of the role to create the SecretID for.

`Metadata` - (Optional) A JSON-encoded string containing metadata in key-value pairs to be set on tokens issued with this SecretID.

`CidrList` - (Optional) If set, specifies blocks of IP addresses which can perform the login operation using this SecretID.

`SecretId` - (Optional) The SecretID to be created. If set, uses "Push" mode.  Defaults to Vault auto-generating SecretIDs.


## Return Values

### Fn::GetAtt

`Accessor` - The unique ID for this SecretID that can be safely logged.

## See Also

* [vault_approle_auth_backend_role_secret_id](https://www.terraform.io/docs/providers/vault/r/approle_auth_backend_role_secret_id.html) in the _Terraform Provider Documentation_