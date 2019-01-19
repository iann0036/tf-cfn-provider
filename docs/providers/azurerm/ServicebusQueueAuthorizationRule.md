# Terraform::AzureRM::ServicebusQueueAuthorizationRule

Manages an Authorization Rule for a ServiceBus Queue.

## Properties

`Name` - (Required) Specifies the name of the Authorization Rule. Changing this forces a new resource to be created.

`NamespaceName` - (Required) Specifies the name of the ServiceBus Namespace in which the Queue exists. Changing this forces a new resource to be created.

`QueueName` - (Required) Specifies the name of the ServiceBus Queue. Changing this forces a new resource to be created.

`ResourceGroupName` - (Required) The name of the Resource Group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.

`Listen` - (Optional) Does this Authorization Rule have Listen permissions to the ServiceBus Queue? Defaults to `false`.

`Send` - (Optional) Does this Authorization Rule have Send permissions to the ServiceBus Queue? Defaults to `false`.

`Manage` - (Optional) Does this Authorization Rule have Manage permissions to the ServiceBus Queue? When this property is `true` - both `Listen` and `Send` must be too. Defaults to `false`.


## Return Values

### Fn::GetAtt

`Id` - The ID of the Authorization Rule.

`PrimaryKey` - The Primary Key for the Authorization Rule.

`PrimaryConnectionString` - The Primary Connection String for the Authorization Rule.

`SecondaryKey` - The Secondary Key for the Authorization Rule.

`SecondaryConnectionString` - The Secondary Connection String for the Authorization Rule.

## See Also

* [azurerm_servicebus_queue_authorization_rule](https://www.terraform.io/docs/providers/azurerm/r/servicebus_queue_authorization_rule.html) in the _Terraform Provider Documentation_