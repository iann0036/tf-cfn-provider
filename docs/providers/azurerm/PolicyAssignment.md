# Terraform::AzureRM::PolicyAssignment

Configures the specified Policy Definition at the specified Scope. Also, Policy Set Definitions are supported.

## Properties

TBC

## Return Values

### Fn::GetAtt

`Id` - The Policy Assignment id.

`Identity` - An `identity` block.

`PrincipalId` - The Principal ID of this Policy Assignment if `type` is `SystemAssigned`.

`TenantId` - The Tenant ID of this Policy Assignment if `type` is `SystemAssigned`.

## See Also

* [azurerm_policy_assignment](https://www.terraform.io/docs/providers/azurerm/r/policy_assignment.html) in the _Terraform Provider Documentation_