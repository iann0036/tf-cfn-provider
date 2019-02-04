# Terraform::Vault::EgpPolicy

Provides a resource to manage Endpoint Governing Policy (EGP) via [Sentinel](https://www.vaultproject.io/docs/enterprise/sentinel/index.html).

**Note** this feature is available only with Vault Enterprise.

## Properties

`Name` - (Required) The name of the policy.

`Paths` - (Required) List of paths to which the policy will be applied to.

`EnforcementLevel` - (Required) Enforcement level of Sentinel policy. Can be either `advisory` or `soft-mandatory` or `hard-mandatory`.

`Policy` - (Required) String containing a Sentinel policy.


## See Also

* [vault_egp_policy](https://www.terraform.io/docs/providers/vault/r/egp_policy.html) in the _Terraform Provider Documentation_