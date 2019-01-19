# Terraform::AzureRM::RoleAssignment

Assigns a given Principal (User or Application) to a given Role.

## Properties

`Name` - (Optional) A unique UUID/GUID for this Role Assignment - one will be generated if not specified. Changing this forces a new resource to be created.

`Scope` - (Required) The scope at which the Role Assignment applies too, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`. Changing this forces a new resource to be created.

`RoleDefinitionId` - (Optional) The Scoped-ID of the Role Definition. Changing this forces a new resource to be created. Conflicts with `RoleDefinitionName`.

`RoleDefinitionName` - (Optional) The name of a built-in Role. Changing this forces a new resource to be created. Conflicts with `RoleDefinitionId`.

`PrincipalId` - (Required) The ID of the Principal (User or Application) to assign the Role Definition to. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The Role Assignment ID.

## See Also

* [azurerm_role_assignment](https://www.terraform.io/docs/providers/azurerm/r/role_assignment.html) in the _Terraform Provider Documentation_