# Terraform::Vault::SshSecretBackendRole

Provides a resource to manage roles in an SSH secret backend
[SSH secret backend within Vault](https://www.vaultproject.io/docs/secrets/ssh/index.html).

## Properties

`Name` - (Required) Specifies the name of the role to create.

`Backend` - (Required) The path where the SSH secret backend is mounted.

`KeyType` - (Required)  Specifies the type of credentials generated by this role. This can be either `otp`, `dynamic` or `ca`.

`AllowBareDomains` - (Optional) Specifies if host certificates that are requested are allowed to use the base domains listed in `AllowedDomains`.

`AllowHostCertificates` - (Optional) Specifies if certificates are allowed to be signed for use as a 'host'.

`AllowSubdomains` - (Optional) Specifies if host certificates that are requested are allowed to be subdomains of those listed in `AllowedDomains`.

`AllowUserCertificates` - (Optional) Specifies if certificates are allowed to be signed for use as a 'user'.

`AllowUserKeyIds` - (Optional) Specifies if users can override the key ID for a signed certificate with the `key_id` field.

`AllowedCriticalOptions` - (Optional) Specifies a comma-separated list of critical options that certificates can have when signed.

`AllowedDomains` - (Optional) The list of domains for which a client can request a host certificate.

`AllowedExtensions` - (Optional) Specifies a comma-separated list of extensions that certificates can have when signed.

`AllowedUsers` - (Optional) Specifies a comma-separated list of usernames that are to be allowed, only if certain usernames are to be allowed.

`DefaultUser` - (Optional) Specifies the default username for which a credential will be generated.

`KeyIdFormat` - (Optional) Specifies a custom format for the key id of a signed certificate.

`MaxTtl` - (Optional) Specifies the Time To Live value.

`Ttl` - (Optional) Specifies the maximum Time To Live value.


## See Also

* [vault_ssh_secret_backend_role](https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_role.html) in the _Terraform Provider Documentation_