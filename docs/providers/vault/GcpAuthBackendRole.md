# Terraform::Vault::GcpAuthBackendRole

Provides a resource to create a role in an [GCP auth backend within Vault](https://www.vaultproject.io/docs/auth/gcp.html).

## Properties

`Role` - (Required) Name of the GCP role.

`Type` - (Required) Type of GCP authentication role (either `gce` or `iam`).

`ProjectId` - (Optional, Deprecated) GCP Project that the role exists within.

`Ttl` - (Optional) Default TTL of tokens issued by the backend.

`MaxTtl` - (Optional) Maximum TTL of tokens issued by the backend.

`Period` - (Optional) Duration in seconds for token.  If set, the issued token is a periodic token.

`Policies` - (Optional) Policies to grant on the issued token.

`Backend` - (Optional) Path to the mounted GCP auth backend.

`BoundServiceAccounts` - (Optional) GCP Service Accounts allowed to issue tokens under this role. (Note: **Required** if role is `iam`We).


## See Also

* [vault_gcp_auth_backend_role](https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend_role.html) in the _Terraform Provider Documentation_