# Terraform::AzureRM::PolicyAssignment

Configures the specified Policy Definition at the specified Scope. Also, Policy Set Definitions are supported.

## Properties

`Name` - (Required) The name of the Policy Assignment. Changing this forces a new resource to be created.

`Scope` - (Required) The Scope at which the Policy Assignment should be applied, which must be a Resource ID (such as Subscription e.g. `/subscriptions/00000000-0000-0000-000000000000` or a Resource Group e.g.`/subscriptions/00000000-0000-0000-000000000000/resourceGroups/myResourceGroup`). Changing this forces a new resource to be created.

`PolicyDefinitionId` - (Required) The ID of the Policy Definition to be applied at the specified Scope.

`Identity` - (Optional) An `Identity` block.

`Location` - (Optional) The Azure location where this policy assignment should exist. This is required when an Identity is assigned. Changing this forces a new resource to be created.

`Description` - (Optional) A description to use for this Policy Assignment. Changing this forces a new resource to be created.

`DisplayName` - (Optional) A friendly display name to use for this Policy Assignment. Changing this forces a new resource to be created.

`Parameters` - (Optional) Parameters for the policy definition. This field is a JSON object that maps to the Parameters field from the Policy Definition. Changing this forces a new resource to be created.

`NotScopes` - (Optional) A list of the Policy Assignment's excluded scopes. The list must contain Resource IDs (such as Subscriptions e.g. `/subscriptions/00000000-0000-0000-000000000000` or Resource Groups e.g.`/subscriptions/00000000-0000-0000-000000000000/resourceGroups/myResourceGroup`).

`Type` - (Required) The Managed Service Identity Type of this Policy Assignment. Possible values are `SystemAssigned` (where Azure will generate a Service Principal for you), or `None` (no use of a Managed Service Identity).


## Return Values

### Fn::GetAtt

`Id` - The Policy Assignment id.

`Identity` - An `Identity` block.

`PrincipalId` - The Principal ID of this Policy Assignment if `Type` is `SystemAssigned`.

`TenantId` - The Tenant ID of this Policy Assignment if `Type` is `SystemAssigned`.

## See Also

* [azurerm_policy_assignment](https://www.terraform.io/docs/providers/azurerm/r/policy_assignment.html) in the _Terraform Provider Documentation_