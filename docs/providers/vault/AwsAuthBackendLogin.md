# Terraform::Vault::AwsAuthBackendLogin

Logs into a Vault server using an AWS auth backend. Login can be
accomplished using a signed identity request from IAM or using ec2
instance metadata. For more information, see the [Vault
documentation](https://www.vaultproject.io/docs/auth/aws.html).

## Properties

TBC

## Return Values

### Fn::GetAtt

`LeaseDuration` - The duration in seconds the token will be valid, relative.

`LeaseStartTime` - The approximate time at which the token was created,.

`Renewable` - Set to true if the token can be extended through renewal.

`Metadata` - A map of information returned by the Vault server about the.

`AuthType` - The authentication type used to generate this token.

`Policies` - The Vault policies assigned to this token.

`Accessor` - The token's accessor.

`ClientToken` - The token returned by Vault.

## See Also

* [vault_aws_auth_backend_login](https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login.html) in the _Terraform Provider Documentation_