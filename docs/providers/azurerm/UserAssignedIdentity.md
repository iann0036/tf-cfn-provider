# Terraform::AzureRM::UserAssignedIdentity

Manages a user assigned identity.

## Properties

`Name` - (Required) The name of the user assigned identity. Changing this forces a
new identity to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to
create the user assigned identity.

`Location` - (Required) The location/region where the user assigned identity is
created.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The user assigned identity ID.

`PrincipalId` - Service Principal ID associated with the user assigned identity.

`ClientId` - Client ID associated with the user assigned identity.

## See Also

* [azurerm_user_assigned_identity](https://www.terraform.io/docs/providers/azurerm/r/user_assigned_identity.html) in the _Terraform Provider Documentation_