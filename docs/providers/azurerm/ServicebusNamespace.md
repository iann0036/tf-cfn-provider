# Terraform::AzureRM::ServicebusNamespace

Manage a ServiceBus Namespace.

## Properties

`Name` - (Required) Specifies the name of the ServiceBus Namespace resource . Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which to create the namespace.

`Location` - (Required) Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

`Sku` - (Required) Defines which tier to use. Options are basic, standard or premium.

`Capacity` - (Optional) Specifies the capacity, can only be set when `Sku` is `Premium` namespace. Can be `1`, `2` or `4`.

`Tags` - (Optional) A mapping of tags to assign to the resource.


## Return Values

### Fn::GetAtt

`Id` - The ServiceBus Namespace ID.

`DefaultPrimaryConnectionString` - The primary connection string for the authorization.

`DefaultSecondaryConnectionString` - The secondary connection string for the.

`DefaultPrimaryKey` - The primary access key for the authorization rule `RootManageSharedAccessKey`.

`DefaultSecondaryKey` - The secondary access key for the authorization rule `RootManageSharedAccessKey`.

## See Also

* [azurerm_servicebus_namespace](https://www.terraform.io/docs/providers/azurerm/r/servicebus_namespace.html) in the _Terraform Provider Documentation_