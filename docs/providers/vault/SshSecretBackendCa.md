# Terraform::Vault::SshSecretBackendCa

Provides a resource to manage CA information in an SSH secret backend
[SSH secret backend within Vault](https://www.vaultproject.io/docs/secrets/ssh/index.html).

## Properties

`Backend` - (Optional) The path where the SSH secret backend is mounted. Defaults to 'ssh'.

`GenerateSigningKey` - (Optional) Whether Vault should generate the signing key pair internally. Defaults to true.

`PublicKey` - (Optional) The public key part the SSH CA key pair; required if generate_signing_key is false.

`PrivateKey` - (Optional) The private key part the SSH CA key pair; required if generate_signing_key is false.


## See Also

* [vault_ssh_secret_backend_ca](https://www.terraform.io/docs/providers/vault/r/ssh_secret_backend_ca.html) in the _Terraform Provider Documentation_