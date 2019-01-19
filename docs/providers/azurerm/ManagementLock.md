# Terraform::AzureRM::ManagementLock

Manages a Management Lock which is scoped to a Subscription, Resource Group or Resource.

## Properties

`Name` - (Required) Specifies the name of the Management Lock. Changing this forces a new resource to be created.

`Scope` - (Required) Specifies the scope at which the Management Lock should be created. Changing this forces a new resource to be created.

`LockLevel` - (Required) Specifies the Level to be used for this Lock. Possible values are `CanNotDelete` and `ReadOnly`. Changing this forces a new resource to be created.

`Notes` - (Optional) Specifies some notes about the lock. Maximum of 512 characters. Changing this forces a new resource to be created.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Management Lock.

## See Also

* [azurerm_management_lock](https://www.terraform.io/docs/providers/azurerm/r/management_lock.html) in the _Terraform Provider Documentation_