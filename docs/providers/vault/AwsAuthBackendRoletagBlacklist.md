# Terraform::Vault::AwsAuthBackendRoletagBlacklist

Configures the periodic tidying operation of the blacklisted role tag entries.

## Properties

`Backend` - (Required) The path the AWS auth backend being configured was mounted at.

`SafetyBuffer` - (Oprtional) The amount of extra time that must have passed beyond the roletag expiration, before it is removed from the backend storage. Defaults to 259,200 seconds, or 72 hours.

`DisablePeriodicTidy` - (Optional) If set to true, disables the periodic tidying of the roletag blacklist entries. Defaults to false.


## See Also

* [vault_aws_auth_backend_roletag_blacklist](https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_roletag_blacklist.html) in the _Terraform Provider Documentation_