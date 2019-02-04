# Terraform::Vault::AwsAuthBackendIdentityWhitelist

Configures the periodic tidying operation of the whitelisted identity entries.

For more information, see the
[Vault docs](https://www.vaultproject.io/api/auth/aws/index.html#configure-identity-whitelist-tidy-operation).

## Properties

`Backend` - (Optional) The path of the AWS backend being configured.

`SafetyBuffer` - (Optional) The amount of extra time, in minutes, that must
have passed beyond the roletag expiration, before it is removed from the
backend storage.

`DisablePeriodicTidy` - (Optional) If set to true, disables the periodic
tidying of the identity-whitelist entries.


## See Also

* [vault_aws_auth_backend_identity_whitelist](https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_identity_whitelist.html) in the _Terraform Provider Documentation_