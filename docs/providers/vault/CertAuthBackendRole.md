# Terraform::Vault::CertAuthBackendRole

Provides a resource to create a role in an [Cert auth backend within Vault](https://www.vaultproject.io/docs/auth/cert.html).

## Properties

`Name` - (Required) Name of the role.

`Certificate` - (Required) CA certificate used to validate client certificates.

`AllowedNames` - (Optional) Allowed subject names for authenticated client certificates.

`AllowedCommonNames` - (Optional) Allowed the common names for authenticated client certificates.

`AllowedDnsSans` - (Optional) Allowed alternative dns names for authenticated client certificates.

`AllowedEmailSans` - (Optional) Allowed emails for authenticated client certificates.

`AllowedUriSans` - (Optional) Allowed URIs for authenticated client certificates.

`AllowedOrganizationUnits` - (Optional) Allowed organization units for authenticated client certificates.

`RequiredExwtensions` - (Optional) TLS extensions required on client certificates.

`Ttl` - (Optional) Default TTL of tokens issued by the backend.

`MaxTtl` - (Optional) Maximum TTL of tokens issued by the backend.

`Period` - (Optional) Duration in seconds for token.  If set, the issued token is a periodic token.

`Policies` - (Optional) Policies to grant on the issued token.

`DisplayName` - (Optional) The name to display on tokens issued under this role.

`BoundCidrs` - (Optional) Restriction usage of the certificates to client IPs falling within the range of the specified CIDRs.

`Backend` - (Optional) Path to the mounted Cert auth backend.


## See Also

* [vault_cert_auth_backend_role](https://www.terraform.io/docs/providers/vault/r/cert_auth_backend_role.html) in the _Terraform Provider Documentation_