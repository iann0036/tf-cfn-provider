# Terraform::Tfe::PolicySet

Sentinel Policy as Code is an embedded policy as code framework integrated
with Terraform Enterprise.

Policy sets are groups of policies that are applied together to related workspaces.
By using policy sets, you can group your policies by attributes such as environment
or region. Individual policies that are members of policy sets will only be checked
for workspaces that the policy set is attached to.

## Properties

`Name` - (Required) Name of the policy set.

`Description` - (Optional) A description of the policy set's purpose.

`Global` - (Optional) Whether or not policies in this set will apply to
all workspaces. Defaults to `false`. This value _must not_ be provided if
`WorkspaceExternalIds` are provided.

`Organization` - (Required) Name of the organization.

`PolicyIds` - (Required) A list of Sentinel policy IDs.

`WorkspaceExternalIds` - (Optional) A list of workspace external IDs. If
the policy set is `Global`, this value _must not_ be provided.


## Return Values

### Fn::GetAtt

`Id` - The ID of the policy set.

## See Also

* [tfe_policy_set](https://www.terraform.io/docs/providers/tfe/r/policy_set.html) in the _Terraform Provider Documentation_