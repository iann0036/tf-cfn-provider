# Terraform::AzureRM::ServicebusNamespaceAuthorizationRule

Manages a ServiceBus Namespace authorization Rule within a ServiceBus.

## Properties

`Name` - (Required) Specifies the name of the ServiceBus Namespace Authorization Rule resource. Changing this forces a new resource to be created.

`NamespaceName` - (Required) Specifies the name of the ServiceBus Namespace. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the resource group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.

`Listen` - (Optional) Grants listen access to this this Authorization Rule. Defaults to `false`.

`Send` - (Optional) Grants send access to this this Authorization Rule. Defaults to `false`.

`Manage` - (Optional) Grants manage access to this this Authorization Rule. When this property is `true` - both `Listen` and `Send` must be too. Defaults to `false`.


## Return Values

### Fn::GetAtt

`Id` - The ServiceBus Topic ID.

`PrimaryKey` - The Primary Key for the ServiceBus Namespace authorization Rule.

`PrimaryConnectionString` - The Primary Connection String for the ServiceBus Namespace authorization Rule.

`SecondaryKey` - The Secondary Key for the ServiceBus Namespace authorization Rule.

`SecondaryConnectionString` - The Secondary Connection String for the ServiceBus Namespace authorization Rule.

## See Also

* [azurerm_servicebus_namespace_authorization_rule](https://www.terraform.io/docs/providers/azurerm/r/servicebus_namespace_authorization_rule.html) in the _Terraform Provider Documentation_