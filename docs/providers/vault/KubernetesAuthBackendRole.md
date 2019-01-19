# Terraform::Vault::KubernetesAuthBackendRole

Manages an Kubernetes auth backend role in a Vault server. See the [Vault
documentation](https://www.vaultproject.io/docs/auth/kubernetes.html) for more
information.

## Properties

`RoleName` - (Required) Name of the role.

`BoundServiceAccountNames` - (Optional) List of service account names able to access this role. If set to "*" all names are allowed, both this and bound_service_account_namespaces can not be "*".

`BoundServiceAccountNamespaces` - (Optional) List of namespaces allowed to access this role. If set to "*" all namespaces are allowed, both this and bound_service_account_names can not be set to "*".

`Ttl` - (Optional) The TTL period of tokens issued using this role in seconds.

`MaxTtl` - (Optional) The maximum allowed lifetime of tokens issued in seconds using this role.

`Period` - (Optional) If set, indicates that the token generated using this role should never expire. The token should be renewed within the duration specified by this value. At each renewal, the token's TTL will be set to the value of this parameter.

`Policies` - (Optional) Policies to be set on tokens issued using this role.

`Backend` - (Optional) Unique name of the kubernetes backend to configure.


## See Also

* [vault_kubernetes_auth_backend_role](https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_role.html) in the _Terraform Provider Documentation_