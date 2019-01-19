# Terraform::AzureRM::ManagementGroup

Manages a Management Group.

## Properties

`GroupId` - (Optional) The UUID for this Management Group, which needs to be unique across your tenant - which will be generated if not provided. Changing this forces a new resource to be created.

`DisplayName` - (Optional) A friendly name for this Management Group. If not specified, this'll be the same as the `GroupId`.

`ParentManagementGroupId` - (Optional) The ID of the Parent Management Group. Changing this forces a new resource to be created.

`SubscriptionIds` - (Optional) A list of Subscription ID's which should be assigned to the Management Group.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Management Group.

## See Also

* [azurerm_management_group](https://www.terraform.io/docs/providers/azurerm/r/management_group.html) in the _Terraform Provider Documentation_