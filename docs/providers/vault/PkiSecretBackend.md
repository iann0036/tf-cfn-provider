# Terraform::Vault::PkiSecretBackend

Creates an PKI Secret Backend for Vault. PKI secret backends can then issue certificates, once a role has been added to
the backend.

## Properties

`Path` - (Required) The unique path this backend should be mounted at. Must not begin or end with a `/`.

`Description` - (Optional) A human-friendly description for this backend.

`DefaultLeaseTtlSeconds` - (Optional) The default TTL for credentials issued by this backend.

`MaxLeaseTtlSeconds` - (Optional) The maximum TTL that can be requested for credentials issued by this backend.


## See Also

* [vault_pki_secret_backend](https://www.terraform.io/docs/providers/vault/r/pki_secret_backend.html) in the _Terraform Provider Documentation_