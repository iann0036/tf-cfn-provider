# Terraform::Vault::RgpPolicy

Provides a resource to manage Role Governing Policy (RGP) via [Sentinel](https://www.vaultproject.io/docs/enterprise/sentinel/index.html).

**Note** this feature is available only with Vault Enterprise.

## Properties

`Name` - (Required) The name of the policy.

`EnforcementLevel` - (Required) Enforcement level of Sentinel policy. Can be either `advisory` or `soft-mandatory` or `hard-mandatory`.

`Policy` - (Required) String containing a Sentinel policy.


## See Also

* [vault_rgp_policy](https://www.terraform.io/docs/providers/vault/r/rgp_policy.html) in the _Terraform Provider Documentation_