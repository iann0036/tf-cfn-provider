# Terraform::Vault::KubernetesAuthBackendConfig

Manages an Kubernetes auth backend config in a Vault server. See the [Vault
documentation](https://www.vaultproject.io/docs/auth/kubernetes.html) for more
information.

## Properties

`KubernetesHost` - (Required) Host must be a host string, a host:port pair, or a URL to the base of the Kubernetes API server.

`KubernetesCaCert` - (Optional) PEM encoded CA cert for use by the TLS client used to talk with the Kubernetes API.

`TokenReviewerJwt` - (Optional) A service account JWT used to access the TokenReview API to validate other JWTs during login. If not set the JWT used for login will be used to access the API.

`PemKeys` - (Optional) List of PEM-formatted public keys or certificates used to verify the signatures of Kubernetes service account JWTs. If a certificate is given, its public key will be extracted. Not every installation of Kubernetes exposes these keys.


## See Also

* [vault_kubernetes_auth_backend_config](https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config.html) in the _Terraform Provider Documentation_