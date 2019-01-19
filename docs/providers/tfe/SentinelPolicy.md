# Terraform::Tfe::SentinelPolicy

Sentinel Policy as Code is an embedded policy as code framework integrated
with Terraform Enterprise.

Policies are configured on a per-organization level and are organized and
grouped into policy sets, which define the workspaces on which policies are
enforced during runs.

## Properties

`Name` - (Required) Name of the policy.

`Description` - (Optional) A description of the policy's purpose.

`Organization` - (Required) Name of the organization.

`Policy` - (Required) The actual policy itself.

`EnforceMode` - (Required) The enforcement level of the policy. Valid values are `advisory`, `hard-mandatory` and `soft-mandatory`. Defaults to `soft-mandatory`.


## Return Values

### Fn::GetAtt

`Id` - The ID of the policy.

## See Also

* [tfe_sentinel_policy](https://www.terraform.io/docs/providers/tfe/r/sentinel_policy.html) in the _Terraform Provider Documentation_